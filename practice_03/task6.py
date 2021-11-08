# 6. Write Python program to find and print factorial of a number
number = int(input('Task 6: Write a number which factorial needs to be found: '))

factorial = 1
for i in range(1, number):
    factorial *= i

print(f'Factorial: {factorial}')
