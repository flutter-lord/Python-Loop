import random

random_num = random.randint(0,100)

your_guess = int(input("\nGuess a number between 0 and 100: "))

while your_guess != random_num:
    