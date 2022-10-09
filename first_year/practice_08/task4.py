# 4. Створіть масив з п'яти прізвищ і виведіть на екран ті,
# які починаються з певної букви, яка вводиться з клавіатури.

# Importing modules
from helpers import getInput
from helpers import colors
import numpy as np
import re

# Getting user input
array = getInput(array_length=5, type=object)

# Continuosly reading user input and
# matching it with array elements
while True:
    user_input = input("Search names:")

    # Generating regex
    input_words = user_input.strip().split(' ')
    search_regex = r"(" + '|'.join(input_words) + ")"

    results = []

    # Searching
    for object in np.nditer(array, flags=["refs_ok"]):
        name = f'{object}'
        if re.match(search_regex, name, re.IGNORECASE):
            results.append(name)

    print('Search results:')
    for i in range(0, len(results)):
        print(f'{results[i]}')

    # Exit case
    if user_input == 'exit':
        break