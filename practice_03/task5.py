# 5. Write a Python Program to reverse a number. For example, if user enters 123
# as input then 321 is printed as output.
numberToReverse = int(input('Task 5: Write a number that we need to reverse: '))
numberLength = len(str(numberToReverse))

resultString = ''
for i in range(1, numberLength + 1):
    # Getting number at this digit
    # and adding it to our resultString
    divider = (10 ** (numberLength - i))
    digit = numberToReverse // divider % 10

    resultString = str(digit) + resultString

print(f'Reversed number: { resultString }')
