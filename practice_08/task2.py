# 2. Введіть з клавіатури п'ять цілочисельних елементів масиву X.
# Виведіть на екран значення коренів і квадратів кожного з елементів масиву.

# Importing modules
from helpers import getInput
import numpy as np

# Getting user input (reuse from task1
array_length = 5
array = getInput(array_length, type=np.int32)

for i in range(0, array_length):
    number = array[i]

    # Calculating root and square and sending
    # them to user
    root = number ** 1/2
    square = number ** 2
    
    print(f'Root and square of {number}: root = {root}; square = {square}')