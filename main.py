
from src.agents.agent import answer_with_agent


def get_help_response():
    return (
        "Welcome to ShopEase Support!\n\n"
        "I can help you with:\n"
        "- Order status and estimated delivery\n"
        "- Refund status and eligibility\n"
        "- Order cancellation eligibility\n"
        "- Connecting you with human support\n\n"
        "Examples:\n"
        "- What is the status of order ORD1002?\n"
        "- What is my refund status for ORD1003?\n"
        "- Can I cancel order ORD1002?\n"
        "- I need to speak to a human."
    )


def main():
    print("=" * 50)
    print("Welcome to ShopEase AI Customer Support!")
    print("Type 'help' for assistance or 'exit' to quit.")
    print("=" * 50)

    thread_id = "shopease-cli-session"

    while True:
        try:
            question = input("\nAsk ShopEase: ").strip()

            if not question:
                print("Please enter a question.")
                continue

            command = question.lower()

            if command in {"exit", "quit"}:
                print("Thank you for contacting ShopEase!")
                break

            if command == "help":
                print("\n" + get_help_response())
                continue

            if command == "clear":
                thread_id = "shopease-cli-new-session"
                print("A new conversation session has started.")
                continue

            if command in {"hi", "hello", "hey"}:
                print(
                    "\nShopEase: Hello! How can I help you today?"
                    "\nType 'help' to see the available support options."
                )
                continue

            if command in {
                "what can you do",
                "what can you help me with",
                "what can you help me with?",
            }:
                print("\n" + get_help_response())
                continue

            print("\nShopEase is processing your request...")

            result = answer_with_agent(
                question,
                thread_id=thread_id,
            )

            print(
                "\nShopEase:",
                result.get(
                    "answer",
                    "Sorry, I couldn't generate an answer.",
                ),
            )

            sources = result.get("sources", [])
            if sources:
                print("\nSources:")
                for source in sources:
                    print("-", source)

        except (KeyboardInterrupt, EOFError):
            print("\nThank you for contacting ShopEase!")
            break

        except Exception:
            print(
                "Sorry, something went wrong. "
                "Please try again later."
            )

        finally:
            print("-" * 50)


if __name__ == "__main__":
    main()
