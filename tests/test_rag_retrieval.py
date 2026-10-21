

from src.retrieval.retriever import get_retriever


def test_rag_retrieval_returns_documents():
    retriever = get_retriever()

    documents = retriever.invoke(
        "What is the refund policy?"
    )

    assert len(documents) > 0

    for document in documents:
        assert isinstance(document.page_content, str)
        assert document.page_content.strip() != ""


def test_rag_retrieval_returns_relevant_content():
    retriever = get_retriever()

    documents = retriever.invoke(
        "What is the refund policy?"
    )

    combined_text = " ".join(
        document.page_content.lower()
        for document in documents
    )

    assert any(
        keyword in combined_text
        for keyword in ["refund", "return", "money"]
    )
