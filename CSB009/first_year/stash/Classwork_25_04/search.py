import unittest

def linear_search(original_list: list, element_to_find: object):
  """
    Linear search algorithm.
    Returns index of element_to_find in original_list, if it exists, otherwise returns -1.
  """
  
  # Looping through array values
  for i in range(0, len(original_list)):
      if original_list[i] == element_to_find:
          return i

  return -1
  
def binary_search(original_list: list, x: object):
  """
    Binary search algorithm.
    Returns index of x, if exists, otherwise returns -1
  """
  
  original_list.sort()
  
  # Array boundaries
  found_index = -1
  left_boundary = 0
  right_boundary = len(original_list) - 1

  while left_boundary <= right_boundary:
    # Comparing center element's and x's values
    center_index = (left_boundary + right_boundary) // 2

    # |-------0--------|
    if original_list[center_index] > x:
      # Updating right boundary
      right_boundary = center_index - 1
    elif original_list[center_index] < x:
      # Updating left boundary
      left_boundary = center_index + 1
    else:
      # Returning found index
      found_index = center_index
      break

  return found_index

def substring_search(string: str, substring: str):
  """
    Subsctring search algorithm.
    Returns start index of substring in string, if exists, otherwise returns -1
  """
  
  start_index = -1
  letter_index = 0

  while (letter_index < len(substring)) and start_index < (len(string) - len(substring)):
    letter_index = 0
    start_index += 1

    while (letter_index < len(substring)) and substring[letter_index] == string[start_index + letter_index]:
      letter_index += 1

  if (letter_index == len(substring)):
    return start_index
  else:
    return -1

  
# Tests
class TestCase(unittest.TestCase):
  # Linear search
  def test_01(self):
    self.assertEqual(linear_search([1,2,3,4,5], 2), 1)
    
  # Binary search
  def test_02(self):
    self.assertEqual(binary_search([1,2,3,4,5,6], 5), 4)
     
  # Substring search
  def test_03(self):
    self.assertEqual(substring_search("Hello world!", "world"), 6)
    
if __name__ == "__main__":
  print("Running tests...")
  unittest.main();