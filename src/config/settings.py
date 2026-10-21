
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQAI_MODEL = os.getenv("GROQAI_MODEL","openai/gpt-oss-120b")


EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-mpnet-base-v2"
)

CHROMA_COLLECTION = os.getenv(
    "CHROMA_COLLECTION",
    "shopease_support"
)