# 1. Напишіть функцію, яка поверне максимальне значення зі списку чисел.

import unittest

def biggest_number(array: list or tuple) -> int:
  # Typechecking
  if not isinstance(array, (list, tuple)):
    raise Exception('Array must be of list or tuple type')

  # Deep typechecking
  # https://stackoverflow.com/a/13252348
  if not all(isinstance(x, (int, float, complex)) for x in array):
    raise Exception('All values in array must be of int, float or complex')

  # Finding biggest number using
  # linear algorithm
  biggest = float('-inf')

  for number in array:
    if number > biggest:
      biggest = number

  return biggest

# Tests
class TestCase(unittest.TestCase):
  def test_1(self):
    return self.assertEqual(biggest_number([0, 1, 2, 3, 4]), 4)

  def test_2(self):
    return self.assertEqual(biggest_number([-1, -2, -3, -4]), -1)

  # Allowed types: lists or int tuples
  def test_3(self):
    return self.assertEqual(biggest_number([0, 1]), 1)

  def test_4(self):
      return self.assertEqual(biggest_number((0, 1)), 1)

  # Error checking
  def test_5(self):
    with self.assertRaises(Exception):
      biggest_number({ 1: 2, 3: 4 })

  def test_6(self):
    with self.assertRaises(Exception):
      biggest_number("string")

  def test_7(self):
    with self.assertRaises(Exception):
      biggest_number((1, "tuple"))

  def test_8(self):
    with self.assertRaises(Exception):
      biggest_number([0, 1, "list"])

unittest.main()