# Task 1:
# Написати програму, яка зчитує 4 числа з клавіатури і виводить на екран найбільше з них.

numbers = []

for i in range(0, 4):
    number = int(input("Впишіть число: "))
    numbers.append(number)

print(f'Найбільше число: {max(numbers)}')

# Task 2:
# Визначити кількість днів в році, який вводить користувач. У високосному році - 366 днів, тоді як в звичайному їх 365.
year = int(input('Впишіть рік: '))

if year % 4:
    if year % 100:
        if year % 400:
            print('Високосний рік, 366 днів')
        else:
            print('Не високосний рік, 365 днів')
    else:
        print('Високосний рік, 366 днів')
else:
    print('Не високосний рік, 365 днів')

# Task 3:
# Трикутник існує тільки тоді, коли сума будь-яких двох його сторін більше третьою. Дано: a, b, c - сторони
# передбачуваного трикутника. Напишіть програму, яка вкаже, чи існує такий трикутник чи ні.

a, b, c = int(input('Впишіть a: ')), int(input('Впишіть b: ')), int(input('Впишіть c: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('Трикутник існує')
else:
    print('Трикутник не існує')

# Task 4:
# Виведіть на екран всі числа в діапазоні від 1 до 100 кратні 7.

for number in range(1, 100, 7):
    print(number)

# Task 5:
# Обчислити за допомогою циклу факторіал числа n
n = int(input('Введіть число: '))

for i in range(1, n + 1):
    n *= i

print(f'Факторіал: {n}')

# Task 6:
# Виведіть на екран «пісочний годинник», максимальна ширина яких зчитується з клавіатури (число непарне). У
# прикладі ширина дорівнює 5.

width = int(input('Впишіть ширину пісочного годинника: '))
side_height = width // 2

# Top side
for i in range(0, side_height):
    line = "*" * (width - (i * 2))
    print(line.center(width))

# Center
print("*".center(width))

# Bottom side
for i in range(1, side_height + 1):
    line = "*" * ((i * 2) + 1)
    print(line.center(width))


# Task 7:
# За допомогою циклів вивести на екран всі прості числа від 1 до 100.
def is_prime(n):
    for divider in range(2, n):
        if (n % divider) == 0:
            return False
    return True


print('Prime numbers:')
for number in range(1, 101):
    if is_prime(number):
        print(number)
