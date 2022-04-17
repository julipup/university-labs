import numpy as np

# @def getInput
# Reads array of {array_length} from user
# and returns it as ndarray of number
def getInput(type = np.int32):
    user_input = str(input("Enter an array of values (splitted by coma):"))
    splitted_input = user_input.split(',')

    array = np.empty(len(splitted_input), dtype=type)

    for i in range(0, len(splitted_input)):
        number = splitted_input[i].strip()
        array[i] = number

    return array
