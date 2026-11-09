def count_passed(scores):
    if not scores:
        raise ValueError("Scores cannot be empty")

    count = 0

    for x in scores:
        if x >= 60:
            count += 1

    return count


def calculate_average(scores):
    if not scores:
        raise ValueError("Scores cannot be empty")

    total = 0

    for x in scores:
        total += x

    return total / len(scores)


def find_highest(scores):
    if not scores:
        raise ValueError("Scores cannot be empty")

    highest = scores[0]

    for x in scores:
        if highest < x:
            highest = x

    return highest


def find_lowest(scores):
    if not scores:
        raise ValueError("Scores cannot be empty")

    lowest = scores[0]

    for x in scores:
        if lowest > x:
            lowest = x

    return lowest