import unittest

def bubble_sort(original_array: list):
  """
    Simple bubble sort algorithm.
    Returns sorted algorithm.
  """
  
  array = original_array.copy()
  
  for i in range(len(original_array) - 1):
    for j in range(0, len(original_array) - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]

  return array

def selection_sort(original_array: list):
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
              
    array[i], array[min_index] = array[min_index], array[i]

  return array
    
def insertion_sort(original_array: list):
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
    
    array[j + 1] = key
  
  return array
  
# Tests
class TestCase(unittest.TestCase):
  # Bubble sort
  def test_01(self):
    self.assertEqual(bubble_sort([5,4,3,2,1]), [1,2,3,4,5])
    
  # Selection sort
  def test_02(self):
    self.assertEqual(selection_sort([5,4,3,2,1]), [1,2,3,4,5])
    
  # Insertion sort
  def test_03(self):
    self.assertEqual(insertion_sort([5,4,3,2,1]), [1,2,3,4,5])
    
if __name__ == "__main__":
  print('Running tests...')
  unittest.main()