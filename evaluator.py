from gemini_client import ask_gemini


def score_response(response):
    """Score a response using basic quality indicators."""

    score = 0

    if len(response) >= 100:
        score += 2

    if len(response) >= 300:
        score += 2

    quality_words = [
        "example",
        "because",
        "therefore",
        "step",
        "important",
        "however"
    ]

    matches = sum(
        word in response.lower()
        for word in quality_words
    )

    score += min(matches, 2)

    if "\n" in response:
        score += 1

    if "." in response:
        score += 1

    if len(response.split()) >= 50:
        score += 2

    return min(score, 10)


def compare_responses(response1, response2):
    """Compare two responses using the basic scoring system."""

    score1 = score_response(response1)
    score2 = score_response(response2)

    if score1 > score2:
        winner = "Response 1"

    elif score2 > score1:
        winner = "Response 2"

    else:
        winner = "Tie"

    return {
        "response_1_score": score1,
        "response_2_score": score2,
        "winner": winner
    }


def ai_evaluate(response1, response2):
    """Use Gemini as an AI judge to evaluate two responses."""

    prompt = f"""
You are an expert AI response evaluator.

Compare the following two responses to the same question.

RESPONSE 1:
{response1}

RESPONSE 2:
{response2}

Evaluate both responses based on:

1. Accuracy
2. Relevance
3. Clarity
4. Completeness
5. Overall quality

Give each response a score from 1 to 10.

Use exactly this format:

Response 1:
Accuracy: X/10
Relevance: X/10
Clarity: X/10
Completeness: X/10
Overall: X/10

Response 2:
Accuracy: X/10
Relevance: X/10
Clarity: X/10
Completeness: X/10
Overall: X/10

Winner: Response 1 or Response 2 or Tie

Reason:
Briefly explain why the winner was selected.
"""

    return ask_gemini(prompt)