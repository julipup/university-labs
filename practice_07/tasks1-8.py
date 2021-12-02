# Task 1
# Implement a script which receives a string and
# replaces all " symbols with ' and vise versa.
# The script should return modified string.
print('Task 1:')

sample_string = "Just a 'sample' string \"yeah yeah yeah\""

# replacing ' to $
sample_string = sample_string.replace('\'', '$')
# replacing " to '
sample_string = sample_string.replace('"', '\'')
# replacing $ to "
sample_string = sample_string.replace('$', '"')

print(sample_string)

# Task 2
# Write a script that checks whether a string is a palindrome or not.
# Returns 'True' if it is palindrome, else 'False'.
#
# To check your implementation you can use strings from here
# (https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).
#
# The script has to ignore special characters, whitespaces and different cases
print('Task 2:')

is_palindrome = False

sample_string = 'madam'
# sample_string = '11/11/11'
reverse_string = sample_string[::-1]

if sample_string == reverse_string:
    is_palindrome = True

result_string = 'palindrome' if is_palindrome == True else 'NOT a palindrome'
print(f'The string {sample_string} is {result_string}')

# Task 3
# Implement a script which works the same as str.split
#
# Note:
# Usage of str.split method is prohibited
print('Task 3:')

sample_string = "Hello there! Nice to see you"


def split(string, split_symbols):
    part = ''
    result = []

    for letter in list(string):
        if letter in split_symbols:
            if part != '': result.append(part)
            part = ''
        else:
            part += letter

    if part != '': result.append(part)

    return result


print(split(sample_string, ' '))

# Task 4
# Implement a script which returns the longest word in the given string.
# The word can contain any symbols except whitespaces (`,\n,\tand so on).
# If there are multiple longest words in the string with a same length return the word that occurs first.
print('Task 4:')

sample_string = "Hello there, fellow, traveller! Nice to see you!"
splitted_string = split(sample_string, [' ', ',', '\n', '!', '.'])

longest_word = ''

print(splitted_string)

for word in splitted_string:
    if len(word) > len(longest_word): longest_word = word

print(f'Longest word: {longest_word} ({len(longest_word)} words)')

# Task 5
# For a positive integer n calculate the result value, which is
# equal to the sum of the odd numbers of n.
#
# Example:
# n = 1234 result = 4
# n = 246 result = 0
print('Task 5:')

sample_number = 1234
# sample_number = 246

odds_sum = 0
for number_string in list(str(sample_number)):
    number = int(number_string)

    if number % 2 != 0:
        odds_sum += number

print(f'Sum of odd digits in number {sample_number} = {odds_sum}')

# Task 6
# Create a script that for a positive integer n calculates
# the result value, which is equal to the sum of
# the “1” in the binary representation of n otherwise, returns None.
#
# Example:
# n = 14 = 1110 result = 3
# n = 128 = 10000000 result = 1
print('Task 6:')

sample_number = 14

binary_number = bin(sample_number)[2:]
digit_sum = 0

for i in list(str(binary_number)): digit_sum += int(i)

print(f'Sum of digit 1 in binary-converted number {sample_number} is: {digit_sum}')

# Task 7
# Once upon a time, on a way through the old wild mountainous west,…
#
# … a man was given directions to go from one point to another.
# The directions were "NORTH", "SOUTH", "WEST", "EAST". Clearly
# "NORTH" and "SOUTH" are opposite, "WEST" and "EAST" too.
#
# Going to one direction and coming back the opposite direction
# right away is a needless effort. Since this is the wild west, with
# dreadfull weather and not much water, it's important to save yourself
# some energy, otherwise you might die of thirst!
#
# How I crossed a mountainous desert the smart way.
#
# The directions given to the man are, for example, the following (depending on the language):
#
# ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
# or
# { "NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST" };
# or
# [North, South, South, East, West, North, West]
#
# You can immediatly see that going "NORTH" and immediately "SOUTH"
# is not reasonable, better stay to the same place! So the task is to
# give to the man a simplified version of the plan. A better plan in this case is simply:
#
# ["WEST"]
# or
# { "WEST" }
# or
# [West]
#
# Other examples:
#
# In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.
#
# The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other,
# therefore, the final result is [] (nil in Clojure).
#
# In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"], "NORTH" and "SOUTH"
# are not directly opposite but they become directly opposite after the reduction of
# "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].
#
# Task
#
# Write a script which will take an array of strings and returns an array of
# strings with the needless directions removed (W<->E or S<->N side by side).
print('Task 7:')

destroyable_directions = [["NORTH", "SOUTH"], ["WEST", "EAST"]]
sample_directions = ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"]
# sample_directions = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]


def annihilate_same_directions(directions):
    to_destroy = []

    for direction in directions:
        index = directions.index(direction)

        if index + 1 < len(directions):
            next_direction = directions[index + 1]

            # Checking if current direction (direction)
            # annihilates next direction (next_direction)
            if [direction, next_direction] in destroyable_directions \
                    or [next_direction, direction] in destroyable_directions:
                # Annihilate them
                to_destroy.append(direction)
                to_destroy.append(next_direction)

    if len(to_destroy) > 0:
        # Destroying
        for direction in to_destroy: directions.remove(direction)

        # Returning
        return annihilate_same_directions(directions)
    else:
        return directions


print(f'Directions: {annihilate_same_directions(sample_directions)}')

# Task 8
# Background:
#
# In Japan, a game called Shiritori is played. The rules are simple,
# a group of people take turns calling out a word whose beginning syllable
# is the same as the previous player's ending syllable. For example,
# the first person would say the word ねこ, and the second player must
# make a word that starts with こ, like　こむぎ. This repeats until a player
# can not think of a word fast enough or makes a word that ends in ん, because
# there are no words that begin with ん　in the Japanese language.
#
# English Shiritori has the same principle, with the first and last
# letters of words. That being said the lose condition is saying a
# word that doesn't start with the previous word's last letter or not
# saying a word quick enough.
#
# For example: apple -> eggs -> salmon -> nut -> turkey ...
#
# Your Task:
# You will be given a list of strings, a transcript of an English
# Shiritori match. Your task is to find out if the game ended early, and
# return a list that contains every valid string until the mistake. If a list
# is empty return an empty list. If one of the elements is an empty string,
# that is invalid and should be handled.
#
# Examples:
# All elements valid:
# The array {"dog","goose","elephant","tiger","rhino","orc","cat"}
# should return {"dog","goose","elephant","tiger","rhino","orc","cat"}
#
# An invalid element at index 2:
# The array {"dog","goose","tiger","cat", "elephant","rhino","orc"}
# should return ("dog","goose") since goose ends in 'e' and tiger starts with 't'
#
# An invalid empty string at index 2:
# The array {"ab","bc","","cd"}
# should return ("ab","bc")
#
# All invalid empty string at index 0:
# The array {"","bc","","cd"}
# should return An Empty List
print('Task 8:')

sample_strings = ["dog", "goose", "tiger", "cat", "elephant", "rhino", "orc"]
# During checking stage in for loop we skip first element of array
result_strings = [sample_strings[0]]

for word in sample_strings:
    index = sample_strings.index(word)

    if index > 0:
        last_word = sample_strings[index - 1]

        if last_word[len(last_word) - 1] != word[0]:
            # Breaking
            break
        else:
            result_strings.append(word)

print(f'Result strings: {result_strings}')