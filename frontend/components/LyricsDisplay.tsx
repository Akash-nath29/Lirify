interface LyricsDisplayProps {
  lyrics: string
}

export default function LyricsDisplay({ lyrics }: LyricsDisplayProps) {
  return (
    <div className="mt-8 p-4 bg-gray-800 rounded-lg">
      <h2 className="text-xl font-semibold mb-4">Generated Lyrics:</h2>
      <pre className="whitespace-pre-wrap">{lyrics}</pre>
    </div>
  )
}

