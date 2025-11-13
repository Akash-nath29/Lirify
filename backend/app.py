"""
Lirify Backend API - AI-Powered Lyrics Generation Service

This FastAPI application provides an endpoint for generating song lyrics using a pre-trained
Keras model. The service processes seed text and generates contextually relevant lyrics
with proper formatting including sections and singer annotations.
"""

# Find out original

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic.main import BaseModel
from keras.models import load_model
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
import re


# Data preprocessing: Load and clean training dataset
data = pd.read_csv("dataset.csv")["Lyrics"]

# Concatenate all lyrics into a single corpus for tokenizer training
lyrics_text = ""
for text in data:
    lyrics_text += text

# Clean the text data by removing metadata tags, converting to lowercase, and removing punctuation
# Remove section markers like [Verse], [Chorus]
lyrics_text = re.sub(r'\[.*?\]', '', lyrics_text)
lyrics_text = lyrics_text.lower()  # Normalize case
# Keep only alphanumeric and whitespace
lyrics_text = re.sub(r'[^\w\s]', '', lyrics_text)


# Initialize FastAPI application
app = FastAPI(
    title="Lirify API",
    description="AI-powered lyrics generation service",
    version="1.0.0"
)

# Initialize and train tokenizer on the lyrics corpus
text_tokenizer = Tokenizer(char_level=False)  # Word-level tokenization
text_tokenizer.fit_on_texts([lyrics_text])

# Load the pre-trained lyrics generation model
model = load_model('lyrics_gen.keras')


# Configure CORS middleware for cross-origin requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restrict to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LyricsRequest(BaseModel):
    """Request model for lyrics generation endpoint"""
    seed: str  # Initial text to start generation from
    length: int  # Number of words to generate


def generate_text(seed_text, next_words, model, tokenizer, max_seq_length):
    """
    Generate lyrics text using the trained model with intelligent formatting.

    Args:
        seed_text (str): Initial text to start generation from
        next_words (int): Number of words to generate
        model: Trained Keras model for text generation
        tokenizer: Fitted tokenizer for text preprocessing
        max_seq_length (int): Maximum sequence length for model input

    Returns:
        str: Generated lyrics with proper formatting
    """
    output_text = seed_text
    line_length = 0
    max_line_length = 10  # Maximum words per line for readability
    current_singer = None
    section_header = None

    for _ in range(next_words):
        # Tokenize and pad the current seed text for model input
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences(
            [token_list], maxlen=max_seq_length-1, padding='pre')

        # Generate next word prediction
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = tokenizer.index_word.get(predicted[0], "")

        # Handle section headers (e.g., [Verse], [Chorus])
        if output_word.startswith("[") and output_word.endswith("]"):
            section_header = output_word
            output_text += f"\n{section_header}\n"
            line_length = 0
            continue

        # Handle singer annotations (e.g., [Singer:])
        if ":" in output_word and output_word.endswith("]"):
            current_singer = output_word
            output_text += f"\n{current_singer}\n"
            line_length = 0
            continue

        # Format line breaks for readability
        if line_length >= max_line_length or output_word == ".":
            output_text += "\n" + output_word
            line_length = 0
        else:
            output_text += " " + output_word
            line_length += 1

        # Update seed text for next iteration
        seed_text += " " + output_word

    return output_text


@app.post("/generate")
async def generate_lyrics(request: LyricsRequest):
    """
    Generate lyrics based on seed text and desired length.

    Args:
        request (LyricsRequest): Contains seed text and generation length

    Returns:
        JSONResponse: Generated lyrics in JSON format
    """
    seed = request.seed
    length = request.length

    # Generate lyrics using the trained model (max_seq_length=50 based on training)
    generated_text = generate_text(seed, length, model, text_tokenizer, 50)

    return JSONResponse(content={"lyrics": generated_text})


@app.get('/generate')
async def generate_lyrics_info():
    """
    Information endpoint for the generate route.

    Returns:
        JSONResponse: Instructions for proper API usage
    """
    return JSONResponse(content={"message": "Please use POST request to generate lyrics."})
