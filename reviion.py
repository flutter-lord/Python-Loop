num1, num2, num3,num4, num5 = eval(input("Enter the first number: "))
n = 5

mean = (num1 + num2 + num3 + num4 + num5) / n

distance = pow((num1 - mean), 2)
distance += pow((num2 - mean), 2)
distance += pow((num3 - mean), 2)
distance += pow((num4 - mean), 2)
distance += pow((num5 - mean), 2)

variance = distance / n
import  math as m
standard_deviation = m.sqrt(variance)

print("The variance for the number", str(num1), str(num2), str(num3), str(num4), str(num5), "is",variance, end = "  ")
print("While the standard deviation", standard_deviation, end = "")
