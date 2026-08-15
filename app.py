from gemini_client import ask_gemini
from openai_client import ask_openai
from evaluator import compare_responses, ai_evaluate
from router import route_question

def get_response(model, prompt):
    if model == "gemini":
        return ask_gemini(prompt)

    return ask_openai(prompt)


def main():

    print("\n=== Dual-LLM AI Assistant ===")
    print("1. Gemini")
    print("2. ChatGPT")
    print("3. Compare Both Models")
    print("4. Auto Router")
    print("5. Test AI Evaluator")

    choice = input("\nChoose an option (1/2/3/4/5): ")

    if choice == "5":
        prompt = ""
    else:
        prompt = input("Enter your question: ")

    # --------------------------------------------------
    # GEMINI
    # --------------------------------------------------

    if choice == "1":

        try:
            response = ask_gemini(prompt)

            print("\n--- GEMINI ---\n")
            print(response)

        except Exception as error:
            print("Gemini failed:", error)

    # --------------------------------------------------
    # CHATGPT
    # --------------------------------------------------

    elif choice == "2":

        try:
            response = ask_openai(prompt)

            print("\n--- CHATGPT ---\n")
            print(response)

        except Exception as error:
            print("ChatGPT failed:", error)

    # --------------------------------------------------
    # COMPARE BOTH
    # --------------------------------------------------

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

    # --------------------------------------------------
    # AUTO ROUTER
    # --------------------------------------------------

    elif choice == "4":

        routing = route_question(prompt)

        model = routing["model"]
        category = routing["category"]
        reason = routing["reason"]

        print("\n--- AUTO ROUTER ---")
        print("Category:", category)
        print("Selected Model:", model.upper())
        print("Reason:", reason)

        try:
            response = get_response(model, prompt)

            print("\n--- RESPONSE ---\n")
            print(response)

        except Exception as error:

            print("\nPrimary model failed:", error)

            fallback_model = (
                "chatgpt"
                if model == "gemini"
                else "gemini"
            )

            print(
                f"\nTrying {fallback_model.upper()} as fallback..."
            )

            try:
                response = get_response(
                    fallback_model,
                    prompt
                )

                print("\n--- FALLBACK RESPONSE ---\n")
                print(response)

            except Exception as fallback_error:
                print(
                    "Fallback model failed:",
                    fallback_error
                )

    # --------------------------------------------------
    # AI EVALUATOR TEST
    # --------------------------------------------------

    elif choice == "5":

        print("\n--- AI EVALUATOR TEST ---")

        response1 = """
        The Waterfall Model is a software development methodology
        where development progresses through sequential phases such
        as requirements, design, implementation, testing, and
        maintenance. Each phase is generally completed before the
        next phase begins.
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

    # --------------------------------------------------
    # INVALID OPTION
    # --------------------------------------------------

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()