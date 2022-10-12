# Напишіть функцію, яка приймає два цілих числа n і k і 
# повертає число, що містить k перших цифр числа n.

import unittest

def getFirstDigits(number: int, length: int):
  sign = 1
  if number < 0:
    sign = -1
    number_string = str(number)[1:len(str(number))]
  else:
    number_string = str(number)

  if len(number_string) >= length:
    return sign * int(number_string[0:length])
  else:
    raise Exception('Length can not be bigger than Number')

# Tests
class TestCase(unittest.TestCase):

  # Get one digit of number
  def test_1(self):
    return self.assertEqual(getFirstDigits(1001, 1), 1)

  # Get two digits of number
  def test_2(self):
    return self.assertEqual(getFirstDigits(1001, 2), 10)

  # Get digits of a negative number
  def test_3(self):
    return self.assertEqual(getFirstDigits(-1001, 2), -10)

  # Raise exception
  def test_4(self):
    with self.assertRaises(Exception):
      getFirstDigits(10, 3)

if __name__ == '__main__':
  unittest.main()
