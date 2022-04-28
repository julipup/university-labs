# Bubble sort
import unittest
from testData import random_array, DefaultTestCase

def bubble_sort(original_array: list, test_case = None):
  """
    Simple bubble sort algorithm.
    Returns sorted algorithm.
  """
  
  array = original_array.copy()
  
  for i in range(len(original_array) - 1):
    for j in range(0, len(original_array) - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]

      # Debug information
      if test_case is not None:
        test_case._swaps_made += 2
        test_case._checks_made += 1
        
  return array

# Testings
class TestCase(DefaultTestCase):
  # test1: Big Array
  def test1(self):
    self.assertEqual(bubble_sort(self._original_array, self), self._ascending_sorted_array)

  # test2: Big ascending sorted array
  def test2(self):
    self.assertEqual(bubble_sort(self._descending_sorted_array, self), self._ascending_sorted_array)
    
  # test3: Big descending sorted array
  def test3(self):
    self.assertEqual(bubble_sort(self._ascending_sorted_array, self), self._ascending_sorted_array)
    
if __name__ == "__main__":
  unittest.main()