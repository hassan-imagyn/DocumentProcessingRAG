class Chunker:
    def __init__(self, chunk_size=500, overlap=50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str):
        """
        Splits the text into chunks with overlapping tokens.
        """
        words = text.split()
        chunks = []
        start = 0

        while start < len(words):
            end = start + self.chunk_size
            chunk = " ".join(words[start:end])
            chunks.append(chunk)

            # Move to next chunk with overlap
            start += self.chunk_size - self.overlap

        return chunks
