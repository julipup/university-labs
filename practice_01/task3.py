# Task #3: Digits of a Number

# Write a Python-script that detects the last 4 digits of a credit card
# 0000 0000 0000 0000 (16 digits) (octagonal number)

# IF credit card number is stored in db as number
credit_card = 0o1234123412340012

# Converting credit_card to octagonal number and then to
# string and getting 4 last digits
last_digits = str(oct(credit_card))[14:]
print(last_digits)  # prints 0012

# OR
# IF credit card number is stored as string
credit_card = "1234123412340012"
last_digits = credit_card[12:]
print(last_digits)  # prints 0012

# Find the sum of the digits of a three-digit number

number = 123
digits_sum = 0

# https://stackoverflow.com/a/4978792
digits = list(str(number))
for digit in digits:
    digits_sum += int(digit)

print(digits_sum)  # prints 6

# OR

# I know that this piece of code is complicated but it's cool 😎
from functools import reduce

number = 123
digits_sum = reduce(lambda a, b: int(a) + int(b), list(str(number)))
print(digits_sum)  # prints 6
