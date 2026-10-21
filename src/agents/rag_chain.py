

from src.agents.llm import get_llm
from src.prompts.qa_prompts import qa_prompt
from src.retrieval.retriever import get_retriever


def answer_question(question: str) -> dict:
    # 1. Retrieve relevant documents
    retriever = get_retriever()
    documents = retriever.invoke(question)

    # 2. Extract and combine the retrieved text
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # 3. Fill the prompt placeholders
    formatted_prompt = qa_prompt.invoke({
        "context": context,
        "question": question,
    })

    # 4. Send the completed prompt to the LLM
    llm = get_llm()
    response = llm.invoke(formatted_prompt)

    # 5. Return the answer and source documents
    return {
        "answer": response.content,
        "sources": [
            document.metadata.get("source", "Unknown")
            for document in documents
        ],
    }


# hide this so that we can use the above created pipe line in other file also
# if __name__ == "__main__":
#     print("Welcome to the AI Customer Support Agent!")
#     print("Type 'exit' to quit.\n")

#     while True:
#         question = input("Ask ShopEase: ").strip()

#         if question.lower() == "exit":
#             print("Thank you for contacting ShopEase!")
#             break

#         if not question:
#             print("Please enter a question.\n")
#             continue

#         print("We will assist you. Please wait...\n")

#         result = answer_question(question)

#         print("Customer question:", question)
#         print("\nAnswer:", result["answer"])
#         print("\nSources:")

#         for source in result["sources"]:
#             print("-", source)

#         print("\n" + "-" * 40 + "\n")
