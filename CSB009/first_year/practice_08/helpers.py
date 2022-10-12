# Importing modules
import sys
import numpy as np

# @def getInput
# Reads array of {array_length} from user
# and returns it as ndarray of number
def getInput(array_length: int, type):
    array = np.empty(array_length, dtype=type)

    user_input = str(input("Enter an array of values (splitted by coma):"))
    splitted_input = user_input.split(',')

    if len(splitted_input) != array_length:
        raise Exception(f'Inputted array is bigger (or smaller) then array length ({array_length})')

    for i in range(0, len(splitted_input)):
        number = splitted_input[i].strip()
        array[i] = number

    return array

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'