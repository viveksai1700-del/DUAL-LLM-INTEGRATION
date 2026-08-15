from gemini_client import ask_gemini
from openai_client import ask_openai


def route_question(prompt):
    prompt_lower = prompt.lower()

    coding_keywords = [
        "code", "python", "java", "javascript",
        "program", "bug", "error", "debug"
    ]

    if any(keyword in prompt_lower for keyword in coding_keywords):
        return "gemini"

    return "gemini"


def main():
    print("\n=== Dual-LLM AI Assistant ===")
    print("1. Gemini")
    print("2. ChatGPT")
    print("3. Auto Router")

    choice = input("\nChoose a model (1/2/3): ")
    prompt = input("Enter your question: ")

    if choice == "1":
        model = "gemini"

    elif choice == "2":
        model = "chatgpt"

    elif choice == "3":
        model = route_question(prompt)

    else:
        print("Invalid choice.")
        return

    print(f"\n--- Using {model.upper()} ---\n")

    try:
        if model == "gemini":
            response = ask_gemini(prompt)

        else:
            response = ask_openai(prompt)

        print(response)

    except Exception as error:
        print(f"{model.upper()} failed: {error}")

        if model == "gemini":
            print("\nTrying ChatGPT as fallback...")

            try:
                print(ask_openai(prompt))
            except Exception:
                print("ChatGPT is currently unavailable.")

        else:
            print("\nTrying Gemini as fallback...")

            try:
                print(ask_gemini(prompt))
            except Exception:
                print("Gemini is currently unavailable.")


if __name__ == "__main__":
    main()