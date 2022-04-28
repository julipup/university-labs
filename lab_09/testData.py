import numpy as np
import unittest
import time

# Randomly generated array
# Available sortings: none, ascending, descending
def random_array(size = 30, sorting = "none"):
  array = np.random.randint(-100, 100, size)
  
  # Sorting
  array.sort() if sorting == "ascending" else array[::-1].sort()
  
  return list(array)

class DefaultTestCase(unittest.TestCase):
  # Time spent information
  def setUp(self):
    # Setting up our array
    array = random_array(1000)
    ascending_sorted_array = array[::]
    descending_sorted_array = array[::-1]
    
    ascending_sorted_array.sort()
    descending_sorted_array.sort()
    
    self._original_array = array
    self._ascending_sorted_array = ascending_sorted_array
    self._descending_sorted_array = descending_sorted_array
    
    self._started_at = time.time()
    
    # Debug information
    self._swaps_made = 0
    self._checks_made = 0
  
  def tearDown(self):
    elapsed = time.time() - self._started_at
    
    # Sort-related information
    if hasattr(self, '_swaps_made') and self._swaps_made is not 0:
      print('{} swaps were made'.format(self._swaps_made))
    
    if hasattr(self, '_checks_made') and self._checks_made is not 0:
      print('{} checks were made'.format(self._checks_made))
    
    print('[{}] Testing done ({}s)'.format(self.id(), round(elapsed, 2)))