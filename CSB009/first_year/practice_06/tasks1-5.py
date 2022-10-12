# Task 1
# Write a Python program to calculate the length of a string.
print('Task 1:')

sample_string = 'Hello World!'
print(f'Length of string "{sample_string}": {len(sample_string)}')

# Task 2
# Write a Python program to get a string made of the first 2
# and the last 2 chars from a given a string. If the string length is
# less than 2, return instead the empty string.
#
# Sample Strings:
# 'w3resource' Expected Result : 'w3ce'
# 'w3' Expected Result : 'w3w3'
# 'w' Expected Result : Empty String
print('Task 2:')

sample_string = "w3resource"
# sample_string = "w3"
# sample_string = "w"

if len(sample_string) > 1:
    print(f'{sample_string[:2]}{sample_string[-2:]}')
else:
    print('')

# Task 3
# Write a Python program to get a string from a given
# string where all occurrences of its first char
# have been changed to '$', except the first char itself.
#
# Sample String: 'restart'
# Expected Result : 'resta$t'
print('Task 3:')

sample_string = 'restart'
# sample_string = 'restartrr'

first_letter = sample_string[0]

print(f'{first_letter}{sample_string[1:].replace(first_letter, "$")}')

# Task 4
# Write a Python function to reverses a string if
# it's length is a multiple of 4.
print('Task 4:')

sample_string = 'multiple of 4'
# sample_string = 'no'

if len(sample_string) % 4 != 0:
    print(sample_string[::-1])
else:
    print(sample_string)

# Task 5
# Write a Python program that accepts a comma separated sequence of
# words as input and prints the unique words in sorted form (alphanumerically).
#
# Sample Words: red, white, black, red, green, black
# Expected Result: black, green, red, white, red
print('Task 5:')

sample_string = 'red, white, black, red, green, black'

words = sample_string.replace(' ', '').split(',')
unique_words = set(sorted(words))

print(f'Unique words (sorted alphanumerically): {", ".join(unique_words)}')
