# Task 4
# Написати програму на мові Python, яка в непорожній послідовності непустих слів з латинських букв визначає
# кількість слів, які починаються і закінчуються однією і тією ж буквою. Результат вивести на екран.

sample_string = 'ама помогите Мадам автобус арА ёмаё'

words = []
for word in sample_string.split(' '):
    if word[0].lower() == word[len(word) - 1].lower():
        words.append(word)

print(f'Words, which starts and ends with the same letter (amount: {len(words)}): {", ".join(words)}')