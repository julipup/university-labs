def degree(number: int, n: int):
  if n == 1:
    return number
  
  return number * degree(number, n - 1)

print(degree(2, 4));

