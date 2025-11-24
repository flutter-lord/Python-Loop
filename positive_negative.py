negative_count, positive_count, average, total_numbers = 0, 0, 0 , 0

integers = eval(input("Enter an integer, the input ends if its is 0: "))
add_up = integers

while integers != 0:
    integers = eval(input("Enter an integer, the input ends if its is 0: "))
    add_up += integers

    if integers < 0:
        negative_count += 1

    else:
        positive_count += 1

    total_numbers = positive_count + negative_count
    average = add_up / total_numbers

print("The number of positive integers is:", positive_count,"\nThe number of negative integers is:", negative_count)
print("The average is:", average)
print("The sum of all the numbers is:", add_up)
print("Total number is:", total_numbers)

