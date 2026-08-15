def evaluate_response(response):
    """
    Evaluates a response based on basic quality indicators.
    Returns a score out of 10.
    """

    score = 0

    if len(response) >= 100:
        score += 2

    if len(response) >= 300:
        score += 2

    if any(word in response.lower() for word in [
        "example", "because", "therefore", "step"
    ]):
        score += 2

    if "\n" in response:
        score += 1

    if "." in response:
        score += 1

    if len(response.split()) >= 50:
        score += 2

    return min(score, 10)


def compare_responses(response1, response2):
    score1 = evaluate_response(response1)
    score2 = evaluate_response(response2)

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