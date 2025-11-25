count = 0
for numbers in range(100, 1001):
    if (numbers % 5 == 0 or numbers % 6 == 0) and not (numbers % 5 == 0 and numbers % 6 == 0):
        print(numbers, end= "  ")
        count += 1

        if count == 10:
            print()
            count = 0