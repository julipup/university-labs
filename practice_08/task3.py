# 3. Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком, починаючи з останнього.

# Importing modules
from helpers import getInput
import numpy as np

# Getting user input
array_length = 5
array = getInput(array_length, type=object)

for i in range(array_length, 0, -1):
    print(array[i - 1])