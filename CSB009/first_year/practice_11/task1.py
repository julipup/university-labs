# Дан масив цілих чисел. Кількість елементів запросити з клавіатури. Знайти:
# - максимальний елемент масиву і його номер;
# - мінімальний елемент масиву.
from helpers import getInput;

array = list(getInput())

# Finding biggest element
biggestElement = array.index(max(array))
print(f'Max element: {array[biggestElement]} (index: {biggestElement})')

lowestElement = array.index(min(array))
print(f'Min element: {array[lowestElement]} (index: {lowestElement})')