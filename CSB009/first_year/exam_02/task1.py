# Task 1. Write a program that given an array of integers determines 
# if it is sorted in "ascending" order, "descending" order or "not sorted" at all.
import enum
import unittest

class ArrayType(enum.Enum):
  ASCENDING = 1
  DESCENDING = 2
  NOT_SORTED = 3

def check_array_type(array: list):
  array_type = None

  if any(not isinstance(element, (int, float)) for element in array):
    raise Exception('Expected array of (int, float)')
  
  for i in range(0, len(array) - 1):
    # Ascending
    if array[i] < array[i + 1]:
      if not array_type:
        array_type = ArrayType.ASCENDING
      elif array_type == ArrayType.DESCENDING:
        # Not sorted 
        return ArrayType.NOT_SORTED

    # Descending
    elif array[i] > array[i + 1]:
      if not array_type:
        array_type = ArrayType.DESCENDING
      elif array_type == ArrayType.ASCENDING:
        # Not sorted
        return ArrayType.NOT_SORTED

  return array_type
    
# Tests
class TestCase(unittest.TestCase):
  # Ascending array
  def test01(self):
    self.assertEqual(check_array_type([1,2,3,4,5]), ArrayType.ASCENDING)
  
  # Descending array
  def test02(self):
    self.assertEqual(check_array_type([5,4,3,2,1]), ArrayType.DESCENDING)
  
  # Not sorted ArrayType
  def test03(self):
    self.assertEqual(check_array_type([1,5,2,1,4]), ArrayType.NOT_SORTED)
  
  # Not integers
  def test04(self):
    with self.assertRaises(Exception):
      check_array_type(["test", 1, 2, 3])
  
if __name__ == "__main__":
  unittest.main()