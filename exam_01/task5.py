# Task 5
# Написати програму на мові Python, яка перевіряє, чи є введене користувачем число
# паліндромом. Примітка: паліндромом називається число, слово або текст,
# які однакового читаються зліва направо і справа наліво.

is_palindrome = False

sample_string = 'madam'
reverse_string = sample_string[::-1]

if sample_string == reverse_string:
    is_palindrome = True

result_string = 'palindrome' if is_palindrome == True else 'NOT a palindrome'
print(f'The string {sample_string} is {result_string}')