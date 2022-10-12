# 1. Введіть з клавіатури в масив п'ять цілочисельних значень.
# Виведіть їх в один рядок через кому. Отримайте для масиву середнє арифметичне.

# Importing modules
from helpers import getInput
import numpy as np

# Getting user input
array = getInput(array_length=5, type=np.int32)

# Writing this array in line (pretty)
string = ""
for i in range(0, len(array)):
    if i != len(array) - 1:
        string += f'{array[i]}, '
    else:
        string += f'{array[i]}'

print(string)

# Finding average (sum first)
sum = 0
for i in range(0, len(array)):
    sum += array[i]

print(f'Average number: {sum/len(array)}')