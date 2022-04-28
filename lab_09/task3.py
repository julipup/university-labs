# Insertion sort
import unittest
from testData import random_array
from testData import DefaultTestCase

def insertion_sort(original_array: list, test_case = None):
  """
    Simple insertion sort algorithm.
    Returns sorted array
  """
  
  array = original_array.copy()
  
  for i in range(1, len(original_array)):
    key = array[i]

    j = i - 1
    
    while j >= 0 and key < array[j] :
      array[j + 1] = array[j]
      j -= 1
      
      # Debug information
      if test_case is not None:
        test_case._swaps_made += 1
    
    array[j + 1] = key
    
    # Debug information
    if test_case is not None:
      test_case._swaps_made += 1
  
  return array

# Testings
class TestCase(DefaultTestCase):
  # test1: Big Array
  def test1(self):
    self.assertEqual(insertion_sort(self._original_array, self), self._ascending_sorted_array)

  # test2: Big ascending sorted array
  def test2(self):
    self.assertEqual(insertion_sort(self._descending_sorted_array, self), self._ascending_sorted_array)
    
  # test3: Big descending sorted array
  def test3(self):
    self.assertEqual(insertion_sort(self._ascending_sorted_array, self), self._ascending_sorted_array)
    
if __name__ == "__main__":
  unittest.main()