# Дан масив 20 цілих чисел на відрізку [-2; 5]. 
# Впорядкувати масив, видаливши нулі із зсувом вліво.
import numpy as np

array = list(np.random.randint(-2, 2, 20))
array.sort()

print(f'Original array: {array}')

# Finding where all 0's are located
if 0 in array:
  leftBound = array.index(0)
  rightBound = len(array) - array[::-1].index(0)
 
  # Deleting all zero's
  array = array[0:leftBound] + array[rightBound:len(array)]

  print(f'New array: {array}')
  print(f'Removed {rightBound - leftBound} zero\'s')
else:
  print("Zero's not found")