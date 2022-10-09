# 1. Імплементувати алгоритм двійкового пошуку значення в массиві та
# продемонструвати працездатність алгоритму.

# Global variables
DEBUG = True

# Importing modules
import numpy as np
from random import randrange
from time import process_time

# Generating and sorting array
array = np.random.randint(0, 100, 100000)
array.sort()

# Generating random value (and placing it somewhere) to find
element = randrange(0, 100)
indexes = np.where(array == element)[0]

# Implementing binary search algorithm
def binary_search(original_list: list, x: object):
  # Array boundaries
  found_index = -1
  left_boundary = 0
  right_boundary = len(original_list) - 1

  # @debug
  iterations = 0

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

    iterations += 1

  if DEBUG is True:
    print(f'Iterations made: {iterations}')

  return found_index

# Capturing start time
start_time = process_time()

# Using implemented function to find element in
# array
found_index = binary_search(array.tolist(), element)
print(f'Index of element {element}: { found_index }')

# Measuring work time
stop_time = process_time()
print(f'Start time: {stop_time}\n'
      f'Stop time: {start_time}\n'
      f'Elapsed time (in seconds): { stop_time - start_time }')

# Testing
assert found_index in indexes