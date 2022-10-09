# 4. Напишіть функцію, яка реалізує лінійний 
# пошук елемента в списку цілих чисел. Якщо такий 
# елемент в списку є, то поверніть його індекс, 
# якщо немає, то поверніть число «-1».

import unittest

def linear_search(array: list or tuple, to_find: int or float or complex) -> int:
  # Typechecking
  if not isinstance(to_find, (int, float, complex)):
    raise Exception('to_find variables must be of int, float of complex type')

  found_index = -1
  for index in range(0, len(array)):
    if array[index] == to_find:
      found_index = index
      break

  return found_index

# Tests
class TestCase(unittest.TestCase):
  def test_1(self):
    return self.assertEqual(linear_search([1, 2, 3, 4], 1), 0)

  def test_2(self):
    return self.assertEqual(linear_search((1, 2, 3, 4), 2), 1)

  def test_3(self):
    return self.assertEqual(linear_search(["array", "number", 3], 3), 2)

  def test_4(self):
    return self.assertEqual(linear_search([1, 2, 3, 4], 5), -1)

  def test_5(self):
    return self.assertEqual(linear_search([1.0, 2.0, 3.0, 4.0], 4.0), 3)

  def test_6(self):
    return self.assertEqual(linear_search([complex(1, 2), complex(3, 4), complex(5, 6)], complex(3, 4)), 1)

  # Error testing
  def test_7(self):
    with self.assertRaises(Exception):
      linear_search([1, 2, 3, 4], "string")

  def test_8(self):
    with self.assertRaises(Exception):
      linear_search([1, 2, 3, 4], ("tuple", "string"))

  def test_9(self):
    with self.assertRaises(Exception):
      linear_search([1, 2, 3, 4], ("4"))

unittest.main()