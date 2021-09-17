"""
Exercise 6: Write a Python-script that calculates the sum, difference and
product of the digits of a three-digit number
"""

# Variables
number = int(input("Enter a n-digit number: "))
length = len(str(number))
digits = []

# Adding number's digits to digits array
for i in range(1, length + 1):
    divider = 10 ** (length - i)
    digits.append(number//divider % 10)

print("Digits:", digits)

# Operations on digits
# - sum
digits_sum = 0
for i in digits:
    digits_sum += i

# - difference
digits_difference = 0
for i in digits:
    digits_difference -= i

# - product
digits_product = 1
for i in digits:
    digits_product *= i

# Printing results
print("Sum of digits:", digits_sum)
print("Difference of digits:", digits_difference)
print("Product of digits:", digits_product)
