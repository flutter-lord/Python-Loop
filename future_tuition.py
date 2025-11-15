NUMBERS_OF_PRIMES = eval(input("Enter the number of prime numbers you want to see: "))
NUMBERS_OF_PRIMES_PER_LINES = 10

count = 0
number = 2

while count < NUMBERS_OF_PRIMES:
    isPrime = True

    divisor = 2

    while divisor <= number // 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1

    if isPrime:
        count += 1

        print(format(number, "5d"), end = "")

        if count % NUMBERS_OF_PRIMES_PER_LINES == 0:
            print()

    number += 1


