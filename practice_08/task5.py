# 5. Створіть масив А [0..7] за
# допомогою генератора випадкових чисел і виведіть його на екран.
# Збільште всі його елементи в 2 рази.

# Importing modules
import numpy as np

# Generating array with size 7 of
# random integers
array = np.random.randint(-100, 100, 7)

print(array)

# Doubling the numbers
with np.nditer(array, op_flags=['readwrite']) as it:
    for x in it:
        x[...] = 2 * x

print(array)