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

# Load and preprocess the lyrics dataset
data = pd.read_csv("data/dataset.csv")["Lyrics"]

lyrics_text = ""

for text in data:
    lyrics_text += text

lyrics_text = re.sub(r'\[.*?\]', '', lyrics_text)
lyrics_text = lyrics_text.lower()
lyrics_text = re.sub(r'[^\w\s]', '', lyrics_text)

# Initialize FastAPI app
app = FastAPI()

# Create and fit the tokenizer
text_tokenizer = Tokenizer(char_level=False)
text_tokenizer.fit_on_texts([lyrics_text])

# Load the model
model = load_model('lyrics_gen.keras')

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LyricsRequest(BaseModel):
    seed: str
    length: int

def generate_text(seed_text, next_words, model, tokenizer, max_seq_length):
    output_text = seed_text
    line_length = 0 
    max_line_length = 10
    current_singer = None
    section_header = None

    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_seq_length-1, padding='pre')
        
        predicted = np.argmax(model.predict(token_list), axis=-1)
        output_word = tokenizer.index_word.get(predicted[0], "")  

        if output_word.startswith("[") and output_word.endswith("]"):
            section_header = output_word
            output_text += f"\n{section_header}\n"
            line_length = 0
            continue
        
        if ":" in output_word and output_word.endswith("]"):
            current_singer = output_word 
            output_text += f"\n{current_singer}\n"
            line_length = 0
            continue

        if line_length >= max_line_length or output_word == ".":
            output_text += "\n" + output_word
            line_length = 0
        else:
            output_text += " " + output_word
            line_length += 1
        
        seed_text += " " + output_word
    
    return output_text
    
@app.post("/generate")
async def generate_lyrics(request: LyricsRequest):
    seed = request.seed
    length = request.length
    generated_text = generate_text(seed, length, model, text_tokenizer, 50)
    return JSONResponse(content={"lyrics": generated_text})
