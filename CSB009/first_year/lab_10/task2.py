# 2. Реалізуйте функцію, параметрами якої є - два 
# числа і рядок. Повертає вона конкатенацію рядки з сумою чисел.

import unittest

def concatenate_numbers(string: str, *numbers: int, divider: str = ' ') -> str:
  # Typechecking
  if not isinstance(string, str):
    raise Exception('String must be of str type')
  
  if not all(isinstance(number, (int, float, complex)) for number in numbers):
    raise Exception('Numbers variable must be of int, float or complex type')
  
  # Concatenating
  string += " "
  for index in range(0 , len(numbers)):
    string += str(numbers[index])

    # Divider
    if (index + 1 < len(numbers)):
      string += divider

  # Returning
  return string

# Tests
class TestCase(unittest.TestCase):
  def test_1(self):
    return self.assertEqual(concatenate_numbers('My age is', 18), 'My age is 18')

  def test_2(self):
    return self.assertEqual(concatenate_numbers('I like', 18, 19), 'I like 18 19')

  def test_3(self):
    return self.assertEqual(concatenate_numbers('Comma numbers:', 1,2,3,4,5,6,7, divider = ','), 'Comma numbers: 1,2,3,4,5,6,7')

  def test_4(self):
    return self.assertEqual(concatenate_numbers('Comma numbers:', 1,2,3,4,5,6,7, divider = ', '), 'Comma numbers: 1, 2, 3, 4, 5, 6, 7')

  # Error checking
  def test_5(self):
    with self.assertRaises(Exception):
      concatenate_numbers(0, 1, 2, 3, 4)

  def test_6(self):
    with self.assertRaises(Exception):
      concatenate_numbers('String', [1,2,3,4])

  def test_7(self):
    with self.assertRaises(Exception):
      concatenate_numbers(("tuple", "second"), 1, 2, 3)

  # ???
  def test_8(self):
    return self.assertEqual(concatenate_numbers(("tuple"), 1, 2, 3), "tuple 1 2 3")

unittest.main()