from random import randint

# Task A (1)
# Дан текст, за яким слідує крапка.
# В алфавітному порядку вивести на екран (по разу)
# усі малі українські голосні букви, що входять в цей текст.

sample_text = "Країна У. Емое"
ukranian_vowels = ['а', 'o', 'у', 'i', 'и', 'е']


def extract_vowels(text: str):
    vowels_list = []
    for letter in list(text):
        if letter in ukranian_vowels:
            vowels_list.append(letter)

    return set(vowels_list)

print(f'Vowels in alph. order: {extract_vowels(sample_text)}')

# Task Б (2)
# Задача. Визначити загальну вартість всіх товарів,
# випущених в поточному році і вивести інформацію про ці
# товари. Поля структури: Найменування, Виробник, Рік випуску, Кількість, Ціна.

# Generator variables
name_start = ["Комп'ютер", "Телефон", "Електросамокат", "Холодильник", "Ложка", "Кружка", "Подушка", "Кровать", "Простирадло", "пес", "Кішка", "Папуга", "Папагей"]
name_middle = ['білий', 'червоний', 'штучний', 'рожевий', 'Xl', 'L', "пір'яна"]
name_end = ['глянцевий', 'гарний', '3G', '4G', '5G', '256GB', '500Gb', 'ігровий', 'штучний']

manufacturer_list = ['Samsung', 'Apple', 'Odzi', 'Google', 'Auto-Owners Insurance', 'Wynn Resorts', 'Pacific Life', 'W.R. Berkley', 'General Electric', 'Alcoa']

items = []


# random items generator
def item_gen():
    # Generating random items properties
    # - name
    name = f'{ name_start[randint(0, len(name_start) - 1)] } ' \
           f'{ name_middle[randint(0, len(name_middle) - 1)] } ' \
           f'{ name_end[randint(0, len(name_end) - 1)] }'

    # - manufacturer
    manufacturer = manufacturer_list[randint(0, len(manufacturer_list) - 1)]

    # - year of issue
    year = randint(2000, 2100)

    # - count
    count = randint(5, 100)

    # - price
    price = randint(10, 10000)

    # Crafting item dict and returning it
    return {
        'name': name,
        'manufacturer': manufacturer,
        'year': year,
        'count': count,
        'price': price
    }


for i in range(2, 20):
    items.append(item_gen())

print('Найменування, Виробник, Рік випуску, Кількість, Ціна')

global_price = 0
for item in items:
    # Calculating global price
    global_price += (item['price'] * item['count'])

    # Printing information about this item
    print(f"{item['name']}, {item['manufacturer']}, {item['year']} р., {item['count']} шт., {item['price']}$")

print(f'Всього продаон товарів на: {global_price}$')
