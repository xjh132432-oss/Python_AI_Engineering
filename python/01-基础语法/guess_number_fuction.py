import random
def generate_number():
    target = random.randint(1, 100)
    return target
def check_number(guess, target):
    if guess == target:
        return 'Correct'
    elif guess > target:
        return "too high"
    else:
        return "too low"
target = generate_number()
while True:
    guess = int(input("please enter your guess: "))
    print(check_number(guess, target))
    if guess == target:
        break