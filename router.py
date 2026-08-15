def route_question(prompt):
    prompt_lower = prompt.lower()

    coding_keywords = [
        "code", "python", "java", "javascript",
        "program", "bug", "error", "debug",
        "function", "algorithm", "syntax"
    ]

    comparison_keywords = [
        "compare", "comparison", "difference between",
        "advantages and disadvantages", "pros and cons"
    ]

    explanation_keywords = [
        "explain", "what is", "define",
        "how does", "why does", "concept", "meaning"
    ]

    if any(keyword in prompt_lower for keyword in coding_keywords):
        return {
            "model": "gemini",
            "category": "Coding",
            "reason": "The question contains programming-related keywords."
        }

    elif any(
        keyword in prompt_lower
        for keyword in comparison_keywords
    ):
        return {
            "model": "gemini",
            "category": "Comparison",
            "reason": "The question requires comparison or evaluation."
        }

    elif any(
        keyword in prompt_lower
        for keyword in explanation_keywords
    ):
        return {
            "model": "gemini",
            "category": "Explanation",
            "reason": "The question asks for an explanation or definition."
        }

    return {
        "model": "gemini",
        "category": "General",
        "reason": "No specialized category was detected."
    }