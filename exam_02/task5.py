# Task 5. Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
import unittest

def convert_to_binary(numbers: list):
  number = 0
  numbers = numbers[::-1]

  for i in range(0, len(numbers)):
    if i == 0:
      digit = 1
    else:
      digit = 2 * i

    # Adding this digit to number
    if numbers[i] == 1: number += digit

  return number

# Tests
class TestCase(unittest.TestCase):
  def test01(self):
    self.assertEqual(convert_to_binary([0, 0, 0, 1]), 1)

  def test02(self):
    self.assertEqual(convert_to_binary([0, 0, 1, 0]), 2)

  def test03(self):
    self.assertEqual(convert_to_binary([0, 0, 1, 1]), 3)

  def test04(self):
    self.assertEqual(convert_to_binary([0, 1, 0, 0]), 4)

if __name__ == "__main__":
  unittest.main()