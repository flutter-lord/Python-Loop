negative_count = 0
positive_count = 0

integers = eval(input("Enter an integer, the input ends if its is 0: "))

while integers != 0:
    integers = eval(input("Enter an integer, the input ends if its is 0: "))

    if integers < 0:
        negative_count += 1

    else:
        positive_count += 1

print("The number of positive integers is:", positive_count,"\nThe number of negative integers is:", negative_count)


