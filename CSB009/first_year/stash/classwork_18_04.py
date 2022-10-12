def even_numbers():
  number = 0
  
  while True:
    yield number
    number += 2
    
generator = even_numbers()
    
for i in range(4):
  print(next(generator))