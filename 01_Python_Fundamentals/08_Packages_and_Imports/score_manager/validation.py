def validate_scores(scores):
    if not scores:
        raise ValueError("Scores cannot be empty")