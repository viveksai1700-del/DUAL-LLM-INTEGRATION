from gemini_client import ask_gemini

prompt = input("Enter your question: ")

print("\n--- Gemini ---")
print(ask_gemini(prompt))