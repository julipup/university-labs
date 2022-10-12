# Сформувати функцію, що буде обчислювати факторіал 
# заданого користувачем натурального числа n.

# Метод рекурсії
def factRec(number: int):
  if number == 0:
    return 1
  else:
    return number * factRec(number - 1)

# Ітераційний метод
def factIter(number: int):
  result = 1;
  
  while number > 0:
    result *= number;
    number -= 1;
    
  return result;
  
  
print(factRec(5))
print(factIter(5))