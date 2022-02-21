# Напишіть функцію аddRightDigit (d, k), яка повинна 
# додавати до цілого позитивного числа K справа цифру D
# (D - цілочисельне значення в діапазоні 0-9, К - цілочисельне значення).

def addRightDigit(number: int, digit: int):
  return int(str(number) + str(digit))

# Tests
print('Performing tests...')

assert addRightDigit(100, 8) == 1008, 'Test 1 failed'
assert addRightDigit(-10, 8) == -108, 'Test 2 failed'
assert addRightDigit(0, 10) == 10, 'Test 3 failed'

print('All tests ran successfully')