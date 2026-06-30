from google import genai
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Gemini's embedding model. 3072 is the max output dimensionality for
# gemini-embedding-001 (matches the original text-embedding-3-large dim
# so the rest of the pipeline / Qdrant config doesn't need to change).
EMBED_MODEL = "gemini-embedding-001"
EMBED_DIM = 3072

splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)


def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)]
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks


def embed_texts(texts: list[str]) -> list[list[float]]:
    # Gemini's batch embedding endpoint
    response = client.models.embed_content(
        model=EMBED_MODEL,
        contents=texts,
        config={"output_dimensionality": EMBED_DIM},
    )
    return [e.values for e in response.embeddings]
