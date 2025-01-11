'use client'

import { useState } from 'react'
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Loader2 } from 'lucide-react'

interface LyricsFormProps {
  onSubmit: (seedText: string, wordCount: number) => void
  isLoading: boolean
}

export default function LyricsForm({ onSubmit, isLoading }: LyricsFormProps) {
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
      <Button type="submit" className="w-full" disabled={isLoading}>
        {isLoading ? (
          <>
            <Loader2 className="mr-2 h-4 w-4 animate-spin" />
            Generating...
          </>
        ) : (
          'Generate Lyrics'
        )}
      </Button>
    </form>
  )
}

