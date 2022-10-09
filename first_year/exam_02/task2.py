# Task 2. Numbers in the Morse code have the following pattern:
# - all digits consist of 5 characters;
# - the number of dots at the beginning indicates the numbers from 1 to 5, the remaining characters are dashes;
# - starting with the number 6, each dot is replaced by a dash and vise versa.
# Write the function morse_number() for encryption of a number in a three-digit format in Morse code.
import unittest

def morse_code(number: int):
  # Checking number size
  if not isinstance(number, int): raise Exception('Integer expected')
  if number < 0 or number > 9: raise Exception('Integer must be between 0 and 9')

  code = ["_", "_", "_", "_", "_"]

  # Numbers from 0 to 5
  for i in range(0, 5):
    if number > i:
      code[i] = "*"

  # Numbers from 6 to 9
  for i in range(0, 4):
    if number > 5 + i:
      code[i] = "_"

  return ''.join(code)

# Tests
class TestCase(unittest.TestCase):
  # Number: 1
  def test1(self):
    self.assertEqual(morse_code(1), "*____")
  
  # Number: 2
  def test2(self):
    self.assertEqual(morse_code(2), "**___")
  # Number: 3
  def test3(self):
    self.assertEqual(morse_code(3), "***__")
  
  # Number: 4
  def test4(self):
    self.assertEqual(morse_code(4), "****_")
  
  # Number: 5
  def test5(self):
    self.assertEqual(morse_code(5), "*****")
  
  # Number: 6
  def test6(self):
    self.assertEqual(morse_code(6), "_****")
  
  # Number: 7
  def test7(self):
    self.assertEqual(morse_code(7), "__***")
  
  # Number: 8
  def test8(self):
    self.assertEqual(morse_code(8), "___**")
  
  # Number: 9
  def test9(self):
    self.assertEqual(morse_code(9), "____*")

  # Number: 0
  def test10(self):
    self.assertEqual(morse_code(0), "_____")

if __name__ == "__main__":
  unittest.main()