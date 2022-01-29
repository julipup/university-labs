# 2. Напишіть програму, що виводить на екран транспоновану
# матрицю 3*3 (початкова матриця задається користувачем)

# Importing modules
from helpers import getInput

# Getting user input
# (user needs to input 3*3 = 9 elements in one array)
print("You need to write 9 elements in one list to create a 3x3 matrix")
array = getInput()

# Checking array size
if array.size != 9:
    raise Exception("Array size isn't 9")

# Reshaping and trans
array = array.reshape(3, 3)
array = array.transpose()

print(array)