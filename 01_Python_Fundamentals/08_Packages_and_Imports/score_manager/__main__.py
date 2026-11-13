from . import (
    calculate_average,
    find_highest,
    find_lowest,
    count_passed
)


def main():
    scores = [90, 85, 92, 88]

    try:
        print(f"Average: {calculate_average(scores):.2f}")
        print(f"Highest: {find_highest(scores)}")
        print(f"Lowest: {find_lowest(scores)}")
        print(f"Passed: {count_passed(scores)}")

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()