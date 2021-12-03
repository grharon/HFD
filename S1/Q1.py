def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


def sum_of_digits(n):
    sum_of_digits = 0
    for digit in str(n):
        sum_of_digits += int(digit)
    return sum_of_digits


number = 100
factorialnumber = factorial(number)
print(f"Factorial({number}) = {factorialnumber}")
sumfactorialnumber = sum_of_digits(factorialnumber)
print(
    f"Sum of digits in the factorial number({number}) = {sumfactorialnumber}")
