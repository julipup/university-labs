# Assume that we define x, y, and z to refer to int values.
# Write an expression that computes whether...

# Defining x,y and z
x, y, z = 4, 5, 5
# x, y, z = 5, -5, 6
# x = y = z = 4


# 1) ...x is odd
print(f'Is x ({x}) odd?: { x % 2 == 0 }')

# 2) ...x is a multiple of 20 (e.g., 20, 40, 60, ...)
print(f'Do x ({x}) is a multiple of 20?: { x % 20 == 0 }')

# 3) ...x and y are both positive
print(f'Is x ({x}) and y ({y}) both positive?: { x >= 0 and y >= 0 }')

# 4) ...x and y have the same sign (both are positive or both are negative)
print(f'Is x ({x}) and y ({y}) have the same sign?: { (x >= 0 and y >= 0) or (x <= 0 and y <= 0) }')

# 5) ...x and y have different signs (one is positive and one is negative)
print(f'Do x ({x}) and y ({y}) have different signs?: { (x >= 0 >= y) or (x <= 0 <= y) }')

# 6) ...all three names (x, y, and z) are bound to equal values
print(f'Do all three variables (x, y and z) are bound to equal values?: { x is y is z }')

# 7) ...all three names (x, y, and z) are bound to different values (none the same)
print(f'Do all three variables (x, y and z) are bound to different values?: { x is not y is not z }')

# 8) ...two variables store the same value, but the third one is different
sorted_numbers = [x, y, z]
sorted_numbers.sort()
print(f'Do two variables store the same value but the third one is different?: '
      f'{ (sorted_numbers[0] == sorted_numbers[1] != sorted_numbers[2]) or (sorted_numbers[1] == sorted_numbers[2] != sorted_numbers[0]) }')
