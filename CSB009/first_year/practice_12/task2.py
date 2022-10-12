# Сформувати функцію для обчислення цифрового кореню натурального числа. 
# Цифровий корінь отримується наступним чином: необхідно скласти всі 
# цифри заданого числа, потім скласти всі цифри знайденої суми і 
# повторювати процес до тих пір, поки сума не буде дорівнювати однозначному 
# числу, що і буде цифровим коренем заданого числа.

import unittest
import time

def getIntegerDigits(number: int):
  if not isinstance(number, (int, float)):
    raise Exception('getIntegerDigits argument must be of type int or float')
    
  return list(map(lambda x: int(x), list(str(int(number)))))

# Метод рекурсії
def digitalRootRec(number: int):
  # Getting digits
  digits = getIntegerDigits(number)
  
  if len(digits) > 1:
    return digitalRootRec(sum(digits))
  else:
    return digits[0]

# Ітераційний метод
def digitalRootIter(number: int):
  digits = getIntegerDigits(number)
  
  while len(digits) > 1:
    digits = getIntegerDigits(sum(digits))
    
  return digits[0]

# Tests
class TestCase(unittest.TestCase):
  # Testing helper function
  def test_1(self):
    return self.assertEqual(getIntegerDigits(10), [1, 0])
  
  def test_2(self):
    return self.assertEqual(getIntegerDigits(110), [1, 1, 0])
  
  def test_3(self):
    return self.assertEqual(getIntegerDigits(100.0), [1, 0, 0])
  
  def test_4(self):
    return self.assertEqual(getIntegerDigits((1)), [1])
  
  def test_5(self):
    with self.assertRaises(Exception):
      getIntegerDigits('string')
  
  # Recursion method tests
  def test_6(self):
    # Timing
    startTime = time.time()
    
    self.assertEqual(digitalRootRec(10), 1)
  
    print('Recursion method performance test time (small number): ', time.time() - startTime)
  
  def test_7(self):
    # Timing
    startTime = time.time()
    
    self.assertEqual(digitalRootRec(6758), 8)
  
    print('Recursion method performance test time (big number): ', time.time() - startTime)
  
  
  def test_8(self):
    # Timing
    startTime = time.time()
    
    self.assertEqual(digitalRootRec(124867293), 6)
  
    print('Recursion method performance test time (huge number): ', time.time() - startTime)
  
  
  # Iteration method tests
  def test_9(self):
    # Timing
    startTime = time.time()
    
    self.assertEqual(digitalRootIter(10), 1)
  
    print('Iteration method performance test time (small number): ', time.time() - startTime)
  
  def test_10(self):
    # Timing
    startTime = time.time()
    
    self.assertEqual(digitalRootIter(6758), 8)
  
    print('Iteration method performance test time (big number): ', time.time() - startTime)
  
  
  def test_11(self):
    # Timing
    startTime = time.time()
    
    self.assertEqual(digitalRootIter(124867293), 6)
  
    print('Iteration method performance test time (huge number): ', time.time() - startTime)
  
unittest.main()