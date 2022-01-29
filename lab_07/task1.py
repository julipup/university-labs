# 1. Напишіть програму, що виводить на екран елементи лінійного
# масиву (елементи масиву задаються користувачем) у зворотному порядку.

# Importing modules
from helpers import getInput

# Getting user input
array = getInput()

for i in range(array.size, 0, -1):
    print(array[i - 1])