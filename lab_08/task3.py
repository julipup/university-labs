# 1. Імплементувати алгоритм пошуку підстроки в строці та
# продемонструвати працездатність алгоритму.


# Implementing algorithm
def substring_search(string: str, substring: str):
  start_index = -1
  letter_index = 0

  while (letter_index < len(substring)) and start_index < (len(string) - len(substring)):
    letter_index = 0
    start_index += 1

    while (letter_index < len(substring)) and substring[letter_index] == string[start_index + letter_index]:
      letter_index += 1

  if (letter_index == len(substring)):
    return start_index
  else:
    return -1


# Tests
# > Test 1
string = 'Hello world!'
substring = 'wo'
assert substring_search(string, substring) is string.find(substring), "Test #1 failed"

# > Test 2
string = 'Hello world!'
substring = 'nope'
assert substring_search(string, substring) is string.find(substring), "Test #2 failed"
