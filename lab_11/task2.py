# Сформувати функцію, що визначатиме чи є задане 
# натуральне число простим. Простим називається число, що 
# більше за 1 та не має інших дільників, окрім 1 та самого себе).
import unittest

def is_simple_number_recursion(number: int, divider = None):
  # Setting up divider variable
  if divider is None:
    divider = number - 1
  
  # Exit conditions
  if divider == 1:
    return True
  
  if number % divider == 0:
    return False
  
  # Recursion itself
  return is_simple_number_recursion(number, divider - 1)

def is_simple_number_iteration(number: int):
  divider = number - 1
  
  while divider > 1:
    if number % divider == 0:
      return False
    
    divider -= 1

  return True
    
# Tests
class TestCase(unittest.TestCase):
  # Recursion method:
  # small number
  def test1(self):
    self.assertEqual(is_simple_number_recursion(11), True)
  
  # Recursion method:
  # Non-simple number
  def test2(self):
    self.assertEqual(is_simple_number_recursion(20), False)
    
  # Recursion method:
  # big number
  def test3(self):
    self.assertEqual(is_simple_number_recursion(97), True)
  
  # Iteration method:
  # small number
  def test4(self):
    self.assertEqual(is_simple_number_iteration(11), True)
    
  # Iteration method:
  # non-simple number
  def test5(self):
    self.assertEqual(is_simple_number_iteration(20), False)
    
  # Iteration method:
  # big number
  def test6(self):
    self.assertEqual(is_simple_number_iteration(97), True)
  
if __name__ == '__main__':
  unittest.main()