# 1. Write a Python program using loop structure to print numbers 1.2.3……9
resultString = ''
for i in range(0, 10):
    postfix = ', ' if (i < 10) else ''
    resultString += f'{i}{postfix}'

print('Task 1: Printing numbers between 1 and 9:\n',
      resultString)

# 2. Write a Python program using loop structure to print numbers 9.8.7…..1
resultString = ''
for i in range(9, 0, -1):
    postfix = ', ' if (i > 1) else ''
    resultString += f'{i}{postfix}'

print('Task 2: Printing numbers between 9 and 1:\n',
      resultString)

# 3. Write a Python program to print on the screen odd numbers between 5..13
resultString = ''
for i in range(5, 14, 2):
    postfix = ', ' if (i < 13) else ''
    resultString += f'{i}{postfix}'

print('Task 3: Printing odd numbers between 5 and 13:\n',
      resultString)

# 4. Write a Python program to add all the numbers entered by a user until user enters 0.
print('Task 4: Write a bunch of random numbers to sum them up or write 0 (zero) to exit.')
sumNumber = 0
while True:
    op = int(input(f'Number (Current Sum: {sumNumber}): '))
    sumNumber += op
    if op == 0:
        break

print(f'Sum: {sumNumber}')
