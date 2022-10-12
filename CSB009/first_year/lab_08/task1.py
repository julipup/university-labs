# 1. Імплементувати алгоритм лінійного пошуку значення в массиві та
# продемонструвати працездатність алгоритму.

from random import randrange
import numpy as np
from time import process_time

# Generating array
array = np.empty(1000, dtype=np.int32)
element = 5

# Setting array's 999 index to element to find
array[999] = element


# Implementing linear search algorithm
def linear_search(original_list: list, element_to_find: object):
    # Looping through array values
    for i in range(0, len(original_list)):
        if original_list[i] == element_to_find:
            return i
        
    return -1


# Capturing start time
start_time = process_time()

# Calling custom linear search algorithm
print(f'Index of element ({element}): { linear_search(array.tolist(), element) }')

# Measuring work time
stop_time = process_time()
print(f'Start time: {start_time}\n'
      f'Stop time: {stop_time}\n'
      f'Elapsed time (in seconds): { stop_time - start_time }')
