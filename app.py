from gemini_client import ask_gemini
from openai_client import ask_openai
from evaluator import compare_responses, ai_evaluate


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
    print("3. Compare Both Models")
    print("4. Auto Router")
    print("5. Test AI Evaluator")

    choice = input("\nChoose an option (1/2/3/4/5): ")
    prompt = input("Enter your question: ") if choice != "5" else ""

    # Gemini
    if choice == "1":
        try:
            response = ask_gemini(prompt)

            print("\n--- GEMINI ---\n")
            print(response)

        except Exception as error:
            print("\nGemini failed:", error)

    # ChatGPT
    elif choice == "2":
        try:
            response = ask_openai(prompt)

            print("\n--- CHATGPT ---\n")
            print(response)

        except Exception as error:
            print("\nChatGPT failed:", error)

    # Compare both models
    elif choice == "3":
        print("\nGetting responses from both models...\n")

        try:
            gemini_response = ask_gemini(prompt)

            print("--- GEMINI ---\n")
            print(gemini_response)

        except Exception as error:
            print("Gemini failed:", error)
            return

        try:
            chatgpt_response = ask_openai(prompt)

            print("\n--- CHATGPT ---\n")
            print(chatgpt_response)

        except Exception as error:
            print("\nChatGPT is unavailable.")
            print("Comparison requires both models.")
            print("Reason:", error)
            return

        result = compare_responses(
            gemini_response,
            chatgpt_response
        )

        print("\n--- RESPONSE COMPARISON ---")
        print(
            "Gemini Score:",
            result["response_1_score"],
            "/ 10"
        )

        print(
            "ChatGPT Score:",
            result["response_2_score"],
            "/ 10"
        )

        print("Winner:", result["winner"])

    # Auto Router
    elif choice == "4":
        model = route_question(prompt)

        print(f"\n--- AUTO ROUTER → {model.upper()} ---\n")

        try:
            if model == "gemini":
                response = ask_gemini(prompt)
            else:
                response = ask_openai(prompt)

            print(response)

        except Exception as error:
            print("Primary model failed:", error)

    # AI Evaluator Test
    elif choice == "5":
        print("\n--- AI EVALUATOR TEST ---")

        response1 = """
        The Waterfall Model is a software development methodology
        where development progresses through sequential phases such
        as requirements, design, implementation, testing, and maintenance.
        Each phase is generally completed before the next phase begins.
        """

        response2 = """
        The Waterfall Model is a sequential development model.
        It starts with requirements and then moves through design,
        coding, testing, deployment, and maintenance. Changes are
        difficult to make once a phase has been completed.
        """

        print("\nEvaluating two sample responses...\n")

        try:
            evaluation = ai_evaluate(
                response1,
                response2
            )

            print("--- AI EVALUATION ---\n")
            print(evaluation)

        except Exception as error:
            print("Evaluator failed:", error)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()