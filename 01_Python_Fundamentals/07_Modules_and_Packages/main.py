import score
def main():
    scores = []

    try:
        print(f"Average:{score.calculate_average(scores)}")
        print(f"Highest:{score.find_highest(scores)}")
        print(f"Lowest:{score.find_lowest(scores)}")
        print(f"Passed:{score.count_passed(scores)}")

    except ValueError:
        print("empty list")
        pass


if __name__ == "__main__":
    main()