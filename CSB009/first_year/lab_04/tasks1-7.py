# 1. Написати програму, яка змінює значення двох цілих змінних a і b без
# використання додаткових змінних.
print('Task 1:')

a = 10
b = 12

print(f'a = {a}, b = {b} (Before change)')

a, b = b, a
print(f'a = {a}, b = {b} (After change)')

# 2. Написати програму, яка обчислює і виводить на екран:
# • середнє арифметичне двох цілих чисел a і b;
# • середнє геометричне двох цілих чисел a і b.
print('Task 2:')

print(f'Average = { (a + b)/2 }')
print(f'Geometric average = { (a * b) * 1/2 }')

# 3. Написати програму, яка переставляє цифри трьохзначного числа, яке задане
# користувачем у зворотному порядку і виводить нове число на екран.
print('Task 3:')

resultString = ''
# Why we need this? To check that user actually wrote a number
# there.
numberToReverse = int(input('Write a number to reverse: '))

# https://stackoverflow.com/a/17380603
for digit in list(str(numberToReverse)):
    resultString = digit + resultString

print(f'Reversed number: {resultString}')

# 4. Написати програму, яка визначає загальну кількість годин доби (змінна hour) і
# загальну кількість хвилин доби (змінна minute), які пройшли до моменту поточної
# секунди доби (змінна second). Наприклад, якщо second = 11111 (second = 3 * 3600
# + 5 * 60 + 11), то hour = 3 і minute = 5.
print('Task 4:')

second = int(input('Write a number of seconds: '))
hour = second // 3600
minute = second // 60 - (hour * 60)

print(f'{hour} hours and {minute} minutes or {second} elapsed')

# 5. Написати програму, яка визначає значення кута в градусах (змінна corner) між
# станом годинникової стрілки на початку доби і її станом в hour годин, minute
# хвилин і second секунд (0 ≤ hour ≤ 11; 0 ≤ minute; second ≤ 59).
print('Task 5:')

# Constant values
hoursAngle = 360 / 12
minutesAngle = hoursAngle / 60
secondsAngle = minutesAngle / 60

# Time values
hour = 11
minute = 11
second = 55

print(f'Angel between 0-hour position and current time: '
      f'{ round((hoursAngle * hour) + (minutesAngle * minute) + (secondsAngle * second), 1) }')

# 6. Написати програму яка визначає чи є натуральне число, що ввів користувач:
# • парним;
# • таким, що закінчується на цифру 5.
print('Task 6:')

number = int(input('Write a number: '))
print('This number is', 'odd' if number % 2 else 'even')
print('...and this number', 'does' if str(number)[len(str(number)) - 1] == '5' else 'doesn\'t', 'end with digit 5.')

# 7. Написати програму, яка визначає значення цілої змінної number - від 1 до 7, в
# залежності від того, на який день тижня (від понеділка до неділі) припадає день
# (ціла змінна day) невисокосного року, в якому 1 січня - понеділок (1 ≤ day ≤ 365).
print('Task 7:')

# Monday
day = 8
days_dictionary = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

while day > 7:
    day -= 7

print(f'Current day: { days_dictionary[day] }')

# Individual Task 1. Написати програму, яка визначає максимальне і мінімальне значення з двох
# різних дробових чисел.
print('Individual Task 1:')

number_01 = 3/5
number_02 = 1/2

# ¯\_(ツ)_/¯
if number_01 > number_02:
    print(f'Number 1 ({number_01}) is bigger than Number 2 ({number_02})')
else:
    print(f'Number 2 ({number_02}) is bigger than Number 1 ({number_01})')