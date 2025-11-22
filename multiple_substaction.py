import random
import sys
import time
correct_count = 0
incorrect_count = 0
count = 0
NUMBER_OF_QUESTIONS = eval(input("How many questions do you want to answer?: "))

start_time = time.time()

while count < NUMBER_OF_QUESTIONS:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    if num1 < num2:
        num1, num2 = num2, num1

    answer = eval(input("What is"+" "+ str(num1) + " - " + str(num2) + ": "))

    if (num1 - num2) == answer:
        print("Wow, Your answers",answer,"is Correct!")
        correct_count += 1

    else:
        print("No,Your answer",answer,"is Incorrect!",)
        print("Your correct answer should be:",(num1 - num2))
        incorrect_count += 1

    continue_question = input("Would you like to continue the question? (y/n): ")
    while continue_question == "n" or continue_question == "N":
        print("This is the end of your test")
        sys.exit()
    count += 1



end_time = time.time()

test_time  = int(end_time - start_time)

print(correct_count,"answers in",NUMBER_OF_QUESTIONS,"questions is correct")
print(incorrect_count,"answers in",NUMBER_OF_QUESTIONS,"questions is incorrect ")
print("\nYou spent", test_time, "secs for the test\n")
