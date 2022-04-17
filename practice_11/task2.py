# Дан масив з 10 елементів. Перші 4 впорядкувати по 
# зростанню, останні 4 по спадаючій.
import numpy as np

array = list(np.random.randint(-10, 10, 10))

print(f'Unsorted array: {array}')

# Sorting first 4 elements
leftPiece = array[0:4]
leftPiece.sort()

# Sorting last 4 elements
rightPiece = array[len(array) - 4:len(array)]
rightPiece.sort(reverse = True)

print(f'Sorted array: {array}')