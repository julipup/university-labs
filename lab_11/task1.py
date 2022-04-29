# Сформувати функцію для введення з клавіатури послідовності чисел 
# і виведення її на екран у зворотному порядку (завершаючий символ послідовності – крапка)
import unittest

def reverse_string_recursive(text):
  if text == "":
    return ""
  else:
    return text[-1] + reverse_string_recursive(text[:-1])

def reverse_string_iterative(text):
  reversed_string = ""
  
  while len(text) != 0:
    reversed_string += text[-1]
    text = text[:-1]
    
  return reversed_string
  
# Tests
class TestCase(unittest.TestCase):
  # Recursive method
  def test1(self):
    self.assertEqual(reverse_string_recursive("Hello world!"), "Hello world!"[::-1])
  
  # Iterative method
  def test2(self):
    self.assertEqual(reverse_string_iterative("Hello world!"), "Hello world!"[::-1])

if __name__ == '__main__':
  unittest.main()