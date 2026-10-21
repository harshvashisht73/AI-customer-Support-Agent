

from src.retrieval.vector_store import (
    get_embedding_model,
    CHROMA_DIR,
)

from langchain_chroma import Chroma


def get_retriever():
    embeddings = get_embedding_model()

    vector_store = Chroma(
        collection_name="shopease_support",
        embedding_function=embeddings,
        persist_directory=str(CHROMA_DIR),
    )

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever


if __name__ == "__main__":
    retriever = get_retriever()

    question = "How can I get a refund for my order?"
    results = retriever.invoke(question)

    print(f"\nQuestion: {question}")
    print(f"Retrieved chunks: {len(results)}\n")

    for index, document in enumerate(results, start=1):
        print(f"--- Result {index} ---")
        print("Source:", document.metadata.get("source"))
        print("Content:", document.page_content)
        print()
