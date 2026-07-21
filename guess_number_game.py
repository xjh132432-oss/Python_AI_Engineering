import random
guess=0
target=random.randint(0,100)
while guess != target:
    guess = int(input("please enter your guess:"))
    if guess < target:
        print("your guess is too low")
    elif guess > target:
        print("your guess is too high")
print("answer is {}".format(target))
