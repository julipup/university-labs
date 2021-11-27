# Task 1
# Write a Python program to generate and print a
# list, where the values are square of numbers between 1 and 30 (both included)
print('Task 1:')

list_squared = []

for i in range(1, 31):
    list_squared.append(i**2)

for number in list_squared:
    print(f'Squared number: {number}')


# Task 2
# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output: The examination will start from : 11/12/2014
print('Task 2:')

exam_st_date = (11, 12, 2014)
print(f'The examination will start from: {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}')

# or
print(f'The examination will start from: {"/".join([str(i) for i in exam_st_date])}')

# Task 3
# Write a Python program which accepts a sequence of comma separated
# numbers from user and generate a list and a tuple with those numbers.
# Sample data: 3, 5, 7, 23
# Output:
# List: ['3', '5', '7', '23']
# Tuple: ('3', '5', '7', '23')
print('Task 3:')

numbers = input('Write any number of numbers separated by commas: ')

numbers_list = numbers.replace(" ", "").split(',')
# or
# generate numbers list while converting
# strings to integers
# numbers_list = [int(number) for number in numbers.split(',')]
numbers_tuple = tuple(numbers_list)

print(f'Numbers list: {numbers_list}')
print(f'Numbers tuple: {numbers_tuple}')

# Task 4
# Write a Python function that takes two lists and returns True
# if they have at least one common member.
print('Task 4:')


def do_contains_similar(list1: list, list2: list):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

# or
# less resource-intensive

# def do_contains_similar(target: list, checkable_list: list):
#     checkable_string = ','.join([str(i) for i in checkable_list]) + ','
#     for checkable_value in target:
#         if checkable_string.find(f'{checkable_value},') >= 0:
#             return True
#     return False


test_list1 = [1, 2, 3, 4]
test_list2 = [0, 0, 0, 0]

print(f'Does {test_list1} contains at least one member of {test_list2}?: {do_contains_similar(test_list1, test_list2)}')

# Task 5
# Write a Python-script.
#
# There is a bus moving in the city, and it takes and drop some people in each bus stop.
#
# You are provided with a list (or array) of integer arrays (or tuples). Each
# integer array has two items which represent number of people get into bus
# (The first item) and number of people get off the bus (The second item) in a bus stop.
# Your task is to return number of people who are still in the bus after the
# last bus station (after the last array). Even though it is the last bus stop,
# the bus is not empty and some people are still in the bus, and they are probably sleeping there :D
#
# Example:
# number([[10,0],[3,5],[5,8]]) # Result is 5
# number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]) # Result is 17
# number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]) # Result is 21
print('Task 5:')

# [[ GOT_ON_BUS, LEFT_THE_BUS ], [...]]

test_info = [[10, 0], [0, 8]] # result is 2
# test_info = [[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]]
# test_info = [[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]]


def bus_migration_result(info: list):
    people_on_bus = 0

    # Looping through all bus stops
    # and performing "very hard"
    # mathematical processes
    for bus_stop in info:
        [got_on_bus, left_the_bus] = bus_stop

        people_on_bus += got_on_bus
        people_on_bus -= left_the_bus

    # Check
    # people_on_bus can not be
    # less than 0
    if people_on_bus < 0:
        people_on_bus = 0

    return people_on_bus


print(f'Result for {test_info}: {bus_migration_result(test_info)}')
