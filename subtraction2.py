import random
import time

NUMBER_OF_QUESTION = eval(input("Enter the number of questions you want to answer: "))
start_time = time.time()
correct_count, incorrect_count, count = 0, 0, 0

while count < NUMBER_OF_QUESTION:
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)

    if num1 < num2:
        num1, num2 = num2, num1

    start_time = time.time()
    answer = eval(input("What is "+ str(num1) + " - " + str(num2) + "? "))
    if answer == (num1 - num2):
        print("Correct!")
        correct_count += 1

    else:
        print("Incorrect!")
        incorrect_count += 1

    count += 1

end_time = time.time()

test_time = int(end_time - start_time)
print("Your test score is: "+ str(correct_count) +" / " + str(NUMBER_OF_QUESTION))
print("And you spent", test_time,"seconds for the test")
print(start_time)
print(end_time)
