from .validation import validate_scores


def calculate_average(scores):
    validate_scores(scores)

    total = 0

    for score in scores:
        total += score

    return total / len(scores)


def find_highest(scores):
    validate_scores(scores)

    highest = scores[0]

    for score in scores:
        if score > highest:
            highest = score

    return highest


def find_lowest(scores):
    validate_scores(scores)

    lowest = scores[0]

    for score in scores:
        if score < lowest:
            lowest = score

    return lowest


def count_passed(scores):
    validate_scores(scores)

    count = 0

    for score in scores:
        if score >= 60:
            count += 1

    return count