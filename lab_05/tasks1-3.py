# Task A (1)
# Одноклітинна амеба кожні 3 години ділиться на 2 клітини.
# Визначити, скільки клітин буде через 3, 6, 9, ..., 24 години,
# якщо спочатку була одна амеба.


def amoeba_count(hours: int):
    # Checking
    if hours <= 0 or hours > 24:
        raise "Error: hours number isn't in range from 0 to 24"

    iterations = hours // 3
    amoeba_sum = 1

    # Progression
    for i in range(iterations):
        amoeba_sum *= 2

    return amoeba_sum


print(f'Amoeba count (3 hours): {amoeba_count(3)}')
print(f'Amoeba count (6 hours): {amoeba_count(6)}')
print(f'Amoeba count (14 hours): {amoeba_count(14)}')
print(f'Amoeba count (24 hours): {amoeba_count(24)}')

# Task Б (2)
# Програма. Дана послідовність, що містить від
# 2 до 20 слів, в кожному з яких від 1 до 5 малих
# латинських букв; між сусідніми словами - не менше
# одного пробілу, за останнім словом - крапка. Вивести
# на екран ті слова послідовності, які відмінні від останнього
# слова, і послідовно розташовані букви слів збігаються
# з початковим відрізком українського алфавіту (а, аб, абв, і т.д.).

# sample_string = ""

# Task В (3)
# Дано речення. Надрукувати його в зворотному порядку слів,
# наприклад, речення «мама мила раму» повинно
# бути надруковано в вигляді «раму мила мама».

sample_string = "мама мила раму"


def reverse_string(string: str):
    words = string.split(' ')
    reversed_words = []

    for word in words:
        reversed_words.insert(0, word)

    return ' '.join(reversed_words)


print(reverse_string(sample_string))