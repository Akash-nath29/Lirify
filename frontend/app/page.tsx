'use client'

import { useState } from 'react'
import LyricsForm from '@/components/LyricsForm'
import LyricsDisplay from '@/components/LyricsDisplay'

export default function Home() {
  const [lyrics, setLyrics] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')

  const generateLyrics = async (seedText: string, wordCount: number) => {
    setIsLoading(true)
    setError('')

    try {
      const response = await fetch('https://lirify-backend-production.up.railway.app/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ seed: seedText, length: wordCount }),
      })

      if (!response.ok) {
        throw new Error('Failed to generate lyrics')
      }

      const data = await response.json()
      setLyrics(data.lyrics)
    } catch (err) {
      setError('An error occurred while generating lyrics. Please try again.')
      console.error(err)
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <main className="min-h-screen bg-gray-900 text-white p-8">
      <div className="max-w-2xl mx-auto">
        <h1 className="text-3xl font-bold mb-8 text-center">AI Lyrics Generator</h1>
        <LyricsForm onSubmit={generateLyrics} />
        {isLoading && <p className="mt-4 text-center">Generating lyrics...</p>}
        {error && <p className="mt-4 text-red-500 text-center">{error}</p>}
        {lyrics && <LyricsDisplay lyrics={lyrics} />}
      </div>
    </main>
  )
}

