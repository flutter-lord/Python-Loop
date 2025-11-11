numbers = eval(input("Enter any digits, the sum end when you input 0: "))
summation = 0

while numbers != 0:
    summation += numbers
    numbers = eval(input("continue inputting any integer: "))

print(summation)