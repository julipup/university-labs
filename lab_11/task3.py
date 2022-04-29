# Сформувати функцію для переведення натурального 
# числа з десяткової системи числення у шістнадцятирічну.
import unittest

def to_binary_recursive(number: int):
  if number < 0:
    raise Exception("Number must be a positive integer")
    
  digit = str(number % 2)
  
  if number > 1:
    return to_binary_recursive(number // 2) + digit
  else:
    return digit
  
def to_binary_iterative(number: int):
  binary_number = ""
  
  while number > 0:
    binary_number += str(number % 2)
    number = number // 2
    
  return binary_number[::-1]
    
# Tests
class TestCase(unittest.TestCase):
  # Recursive method
  def test1(self):
    self.assertEqual(to_binary_recursive(123), format(123, "b"))
  
  # Iterative method
  def test2(self):
    self.assertEqual(to_binary_iterative(123), format(123, "b"))
  
if __name__ == "__main__":
  unittest.main()