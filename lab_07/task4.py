# 4. Напишіть програму, що у матриці 4*4 змінює всі від’ємні елементи на 0

# Importing modules
import numpy as np

# Generating array
array = np.random.randint(-100, 100, (4, 4))

# Looping through array numbers and changing them
with np.nditer(array, op_flags=['readwrite']) as elements:
    for number in elements:
        if number < 0:
            number[...] = 0

print(array)