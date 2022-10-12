# Selection sort
import unittest
from testData import random_array
from testData import DefaultTestCase

def selection_sort(original_array: list, test_case = None):
  """
    Simple selection sort algorithm.
    Returns sorted array.
  """
  
  array = original_array.copy()
  
  for i in range(len(original_array)):    
    min_index = i
    
    for j in range(i + 1, len(original_array)):
      if array[min_index] > array[j]:
        min_index = j
      
      # Debug information
      if test_case is not None:
        test_case._checks_made += 1
              
    array[i], array[min_index] = array[min_index], array[i]
    
    # Debug information
    if test_case is not None:
      test_case._swaps_made += 2
    
  return array

# Testings
class TestCase(DefaultTestCase):
  # test1: Big Array
  def test1(self):
    self.assertEqual(selection_sort(self._original_array, self), self._ascending_sorted_array)

  # test2: Big ascending sorted array
  def test2(self):
    self.assertEqual(selection_sort(self._descending_sorted_array, self), self._ascending_sorted_array)
    
  # test3: Big descending sorted array
  def test3(self):
    self.assertEqual(selection_sort(self._ascending_sorted_array, self), self._ascending_sorted_array)
    
if __name__ == "__main__":
  unittest.main()