

from pathlib import Path
from langchain_community.document_loaders import (
    DirectoryLoader,
    TextLoader,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DOCUMENTS_DIR = PROJECT_ROOT / "data" / "documents"


def load_documents():
    loader = DirectoryLoader(
        str(DOCUMENTS_DIR),
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )

    documents = loader.load()
    return documents


# if __name__ == "__main__":
#     documents = load_documents()

#     print("Total documents loaded:", len(documents))

    # for document in documents:
    #     print("\nSource:", document.metadata["source"])
    #     print("Content preview:", document.page_content[:150])



from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )

    chunks = text_splitter.split_documents(documents)
    return chunks



def prepare_documents(chunks):
    prepared_chunks = []

    for index, chunk in enumerate(chunks):
        source_path = Path(chunk.metadata["source"])

        # Keep only the source filename in metadata.
        chunk.metadata["source"] = source_path.name

        # Give every chunk a unique ID.
        chunk.metadata["chunk_id"] = (
            f"{source_path.stem}_{index}"
        )

        prepared_chunks.append(chunk)

    return prepared_chunks



if __name__ == "__main__":
    documents = load_documents()
    chunks = split_documents(documents)
    prepared_chunks = prepare_documents(chunks)

    print("Documents loaded:", len(documents))
    print("Chunks created:", len(chunks))
    print("Prepared chunks:", len(prepared_chunks))

    if prepared_chunks:
        print("\nFirst prepared chunk:")
        print("Content:", prepared_chunks[0].page_content)
        print("Metadata:", prepared_chunks[0].metadata)