import random

num1 = random.randint(0, 9)
num2 = random.randint(0, 9)

if num1 < num2:
    num1, num2 = num2, num1

answer = num1 - num2

your_answer = eval(input("What is" + " "+ str(num1) + " -" + " " + str(num2) + ": "))

while your_answer != (num1 - num2):
    your_answer = eval(input("No,You are wrong Give the correct answer. "
                             "What is" + " " + str(num1) + " -" + " " + str(num2) + ": "))

print("\nYes!! you are right", num1,"-", num2, "is",your_answer)



