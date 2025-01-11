'use client'

import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"

interface LyricsFormProps {
  onSubmit: (seedText: string, wordCount: number) => void
}

export default function LyricsForm({ onSubmit }: LyricsFormProps) {
  const [seedText, setSeedText] = useState('')
  const [wordCount, setWordCount] = useState(100)

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    onSubmit(seedText, wordCount)
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <Label htmlFor="seedText">Seed Text</Label>
        <Textarea
          id="seedText"
          value={seedText}
          onChange={(e) => setSeedText(e.target.value)}
          placeholder="Enter seed text for your lyrics..."
          className="mt-1"
          required
        />
      </div>
      <div>
        <Label htmlFor="wordCount">Word Count</Label>
        <Input
          type="number"
          id="wordCount"
          value={wordCount}
          onChange={(e) => setWordCount(parseInt(e.target.value))}
          min={1}
          className="mt-1"
          required
        />
      </div>
      <Button type="submit" className="w-full">Generate Lyrics</Button>
    </form>
  )
}

