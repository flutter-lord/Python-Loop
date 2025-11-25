NUMBER_OF_STUDENTS = eval(input("Enter the number of students you wan to input their scores: "))
count, highest_score = 0, 0

while count < NUMBER_OF_STUDENTS:
    student_score = eval(input("Enter the student score: "))

    if student_score > highest_score:
        highest_score = student_score

    count += 1

print("The highest score is: ", highest_score)