

from langchain_groq import ChatGroq

from src.config.settings import GROQAI_MODEL

from src.prompts.qa_prompts import qa_prompt


def get_llm():
    llm = ChatGroq(
        model=GROQAI_MODEL,
        temperature=0
    )

    return llm


if __name__ == "__main__":
    llm = get_llm()
    formatted_prompt = qa_prompt.invoke({
        "context": ("Customers can request a refund within",
        "7 days of delivery."),
        "question":(
            "How many days do I have to request a refund?"
        )
    })
    response = llm.invoke(formatted_prompt)

    print("Answer:", response.content)
