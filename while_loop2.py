import random

number = random.randint(0,2)

while True:
    guess = int(input("Guess a number between 0 and 2: "))

    if guess < number:
        print("Too low!")
        break

    elif guess > number:
        print("Too high!")
        break

