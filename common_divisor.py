num1, num2 = eval(input("Enter the two values you want to find the HCF for: "))

hcf = 1
k = 2

while k <= num1 and k <= num2:
    if num1 % k == 0 and num2 % k == 0:
        hcf = k
    k += 1

print("The highest common factor of", num1, "and", num2, "is", hcf)

