import random

random_num = random.randint(1,100)
print(random_num)

your_guess = int(input("Guess a number between 0 and 100: "))

while your_guess != random_num:

    if your_guess < random_num:
        your_guess = int(input("You guess lower, Guess again: "))

        if 0 < your_guess and random_num - your_guess <= 10:
            print("You are near, Move a bit up")

        else:
            print("Move forward")


    else:
        your_guess = int(input("You are higher, Guess again: "))

        if 0 < random_num and your_guess - random_num <= 10:
            print("You are near, Move a bit down")

        else:
            print("Move backward")

print("You guessed right!")

