# Task 3. Write a function using recursion to check if a number 
# n is prime (you have to check whether n is divisible by any number below n).
import unittest

def is_prime(number: int, check_number = None):
  if not isinstance(number, int):
    raise Exception('Number must be integer')
    
  if number <= 0:
    raise Exception('Number must be positive')
  
  if not check_number:
    check_number = number - 1
  
  # Recursion
  if check_number == 1:
    return True
  else:
    if number % check_number != 0:
      return is_prime(number, check_number - 1)
    else:
      return False
  
    
# Tests
class TestCase(unittest.TestCase):
  # Prime number
  def test01(self):
    self.assertEqual(is_prime(5), True)
  
  # Not prime number
  def test02(self):
    self.assertEqual(is_prime(6), False)
  
  # Not integer
  def test03(self):
    with self.assertRaises(Exception):
      is_prime(5.6)
      
    with self.assertRaises(Exception):
      is_prime("Hello there!")
  
  # Negative number
  def test04(self):
    with self.assertRaises(Exception):
      is_prime(-5)

if __name__ == "__main__":
  unittest.main()