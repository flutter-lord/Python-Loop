NUMBER_OF_STUDENTS = eval(input("Enter the number of students you want to input their scores: "))
count, second_highest_score = 0, 0

student_score = eval(input("Enter the student score: "))
highest_score = student_score

while count < NUMBER_OF_STUDENTS - 1:
    student_score = eval(input("Enter the studentjhgfdcvbnjhgfgh score: "))

    if student_score > highest_score:
        second_highest_score = highest_score
        highest_score = student_score

    elif student_score < highest_score:
        if student_score > second_highest_score:
            second_highest_score = student_score

        else :
            second_highest_score = second_highest_score

    count += 1

print("The highest score is: ", highest_score)
print("The second highest score is: ", second_highest_score)
print()