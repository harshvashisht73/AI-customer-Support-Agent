
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from src.config.settings import EMBEDDING_MODEL

from src.ingestion.load_documents import (
    load_documents,
    split_documents,
    prepare_documents,
)

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
CHROMA_DIR = PROJECT_ROOT / "data" / "chroma_db"


def get_embedding_model():
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )
    return embeddings


def create_vector_store():
    documents = load_documents()
    chunks = split_documents(documents)
    prepared_chunks = prepare_documents(chunks)

    embeddings = get_embedding_model()

    vector_store = Chroma.from_documents(
        documents=prepared_chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
        collection_name="shopease_support",
    )

    return vector_store


if __name__ == "__main__":
    vector_store = create_vector_store()

    print("Vector store created successfully!")
    print("Database location:", CHROMA_DIR)
    print("Number of chunks stored:", vector_store._collection.count())
