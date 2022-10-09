# 1. Матрицю 10x20 заповнити випадковими числами від 0 до 15.
# Вивести на екран саму матрицю і номера рядків, в яких число 5 зустрічається три і більше разів.
import numpy as np

# Generating matrix
matrix = np.random.randint(0, 15, (10, 20))

print(matrix)

# Search algorithm (linear search)
found_elements = []

for x in range(0, len(matrix)):
    row = matrix[x]
    length = len(row)
    found_indexes = []

    # Finding all occurrences
    for y in range(0, length):
        if row[y] == 5:
            found_indexes.append(y)

    if len(found_indexes) >= 3:
        found_elements.append((x, found_indexes))

# Printing found elements
for element in found_elements:
    row_index = element[0]
    numbers_indexes = element[1]

    print(f'Found { len(numbers_indexes) } fives in row with index { row_index } ({ matrix[row_index] })')
