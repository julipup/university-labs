# a) Дан двійковий файл f, компоненти якого є цілими ненульовими числами, причому 
# кількість від'ємних чисел дорівнює кількості додатних, а загальне число 
# компонентів кратне 5. Використовуючи допоміжний файл h, переписати в 
# порядку проходження компоненти файлу f в файл g - три додатних, три від'ємних, три додатних, три від'ємних і так далі.

import struct
from random import randint, shuffle

def write_to_file(numbers: list):
  file = open('input.bin', 'wb')
  file.write(struct.pack(f'{len(numbers)}i', *numbers))
  file.close()

def read_from_file(format: str):
  file = open('input.bin', 'rb')
  content = file.read()
  unpacked = struct.unpack(format, content)
  return unpacked

if __name__ == "__main__":
  # Options
  rewrite_file = True
  array_length = 16 # number of same number sign (must be devidable by 2)

  # Rewriting file (if needed)
  if rewrite_file is True:
    # Variables
    original_numbers = []

    # Generating numbers
    for limit in [(-100, 0), (0, 100)]:
      for i in range(0, int(array_length / 2)):
        original_numbers.append(randint(limit[0], limit[1]))

    # Shuffling and writing all numbers to file
    shuffle(original_numbers)
    write_to_file(original_numbers)

  # Reading numbers from file
  numbers = list(read_from_file(f'{array_length}i'))
  numbers_buffer = []
  output_numbers = []
  
  print('Numbers:', numbers);

  # Generating output file
  while len(numbers) > 0:
    if len(numbers_buffer) <= 0:
      numbers_buffer.append(numbers[0])
      numbers = numbers[1::]
  
    is_positive = True if numbers_buffer[0] >= 0 else False
  
    # Finding number with same number sign
    found_numbers = list(filter(lambda x: True if (is_positive and x >= 0) or (not is_positive and x < 0) else False, numbers))
    if len(found_numbers) >= 2:
      numbers_buffer += found_numbers[:2:]
      
      # Removing this numbers
      for number in numbers_buffer: numbers.remove(number) if number in numbers else None

      # Writing this numbers into file
      output_numbers += numbers_buffer
      
      numbers_buffer = []
    else:
      print('Unused numbers:', found_numbers + numbers_buffer)
      numbers = []
  
  print('Output numbers:', output_numbers)

  # Writing numbers to file
  output_file = open('output.bin', 'wb')
  output_file.write(struct.pack(f'{len(output_numbers)}i', *output_numbers))
  output_file.close()