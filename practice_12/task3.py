# Сформувати функцію для обчислення індексу максимального елемента масиву n*n, де 1<=n<=5.
import numpy as np
from random import randint

height = randint(1, 5)
width = randint(1, 5)
matrix = np.random.randint(-10, 10, size = (height, width))

def matrix_max(matrix, x, y, current_maximum = (0, 0)):
  # Updating maximum value index
  if matrix[x, y] > matrix[current_maximum]:
    current_maximum = (x, y)
  
  # Checking current position
  if y > 0:
    x -= 1;
    
    if x < 0:
      x = matrix.shape[0] - 1
      y -= 1;
  else:
    return current_maximum
    
  # Recursive function
  return matrix_max(matrix, x, y, current_maximum)
  
maximum_value_index = matrix_max(matrix, height - 1, width - 1)
print(f'Matrix: {matrix}')
print(f'Maximum value: {matrix[maximum_value_index]} (index: {maximum_value_index})')