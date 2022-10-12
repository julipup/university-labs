# Task 3
# Написати програму на мові Python, що виводить в стандартний потік
# виведення кількість чисел, які кратні 4.

# numbers_limit = 24
# numbers_limit = 1200
numbers_limit = 23000


# Simple and not a resource-intensive approach
amount = round(numbers_limit / 4)

print(f'Amount of numbers between 0 and {numbers_limit} which is dividable by 4: {amount}')

# or
# A resource-intensive approach
amount = 0
current_number = 0
while current_number < numbers_limit:
    current_number += 1
    if current_number % 4 == 0:
        amount += 1

print(f'Amount: {amount}')
