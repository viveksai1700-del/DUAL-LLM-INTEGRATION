from gemini_client import ask_gemini
from openai_client import ask_openai
from evaluator import compare_responses


def route_question(prompt):
    prompt_lower = prompt.lower()

    coding_keywords = [
        "code", "python", "java", "javascript",
        "program", "bug", "error", "debug"
    ]

    if any(keyword in prompt_lower for keyword in coding_keywords):
        return "gemini"

    return "gemini"


def get_response(model, prompt):
    if model == "gemini":
        return ask_gemini(prompt)

    return ask_openai(prompt)


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
        response = get_response(model, prompt)
        print(response)

        # Evaluate the response
        result = compare_responses(response, response)

        print("\n--- Evaluation ---")
        print("Response 1 Score:", result["response_1_score"])
        print("Response 2 Score:", result["response_2_score"])
        print("Winner:", result["winner"])

    except Exception as error:
        print(f"{model.upper()} failed: {error}")

        fallback_model = "chatgpt" if model == "gemini" else "gemini"

        print(f"\nTrying {fallback_model.upper()} as fallback...\n")

        try:
            response = get_response(fallback_model, prompt)
            print(response)

            result = compare_responses(response, response)

            print("\n--- Evaluation ---")
            print("Response 1 Score:", result["response_1_score"])
            print("Response 2 Score:", result["response_2_score"])
            print("Winner:", result["winner"])

        except Exception as fallback_error:
            print(f"{fallback_model.upper()} fallback failed: {fallback_error}")


if __name__ == "__main__":
    main()