number = eval(input("Enter an integer: "))
maximum = number
while number != 0:
    number = eval(input("Enter an integer: "))
    if number > maximum:
        maximum= number
print("max is", maximum)