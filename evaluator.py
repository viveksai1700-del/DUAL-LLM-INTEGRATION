def score_response(response):
    """Score a response based on basic quality indicators."""

    score = 0

    # Length and completeness
    if len(response) >= 100:
        score += 2

    if len(response) >= 300:
        score += 2

    # Explanation quality
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

    # Structure
    if "\n" in response:
        score += 1

    if "." in response:
        score += 1

    # Vocabulary / detail
    if len(response.split()) >= 50:
        score += 2

    return min(score, 10)


def compare_responses(response1, response2):
    """Compare two AI responses and determine the stronger response."""

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