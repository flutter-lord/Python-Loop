count = 0
for number in range(100, 1001):

    if number % 5 == 0 and number % 6 == 0:
        count += 1
        print(number, end= " ")

        if count == 10:
            print()
            count = 0