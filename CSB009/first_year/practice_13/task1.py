# 1. У текстовому файлі знаходяться записи про номери телефонів. 
# У кожному рядку записана інформація: номер телефону, ПІБ, адреса.
#
# Напишіть програму яка сортує записи в файлі в порядку зростання номера телефону.
from os.path import isfile

def fetch_entries(file, field_names = ()):
  if not isfile(file):
    raise Exception(f'File {file} not found.')
  
  with open(file, 'r') as file:
    entries = []

    line = True
    while bool(line):
      line = file.readline()
      splitted_line = line.split(';')

      if len(splitted_line) >= len(field_names):
        entry = {}
        
        # Addining information about this user to our list
        for value in splitted_line:
          entry[field_names[splitted_line.index(value)]] = value.strip()
          
        entries.append(entry)

    return entries

  
# Looping through all entries
file_name = 'db.txt'
entries = sorted(fetch_entries(file_name, ("phone", "name", "address")), key = lambda x: x['phone'])

# Rewritting this file
with open(file_name, 'w') as file:
  for entry in entries:
    file.write(f'{entry["phone"]}; {entry["name"]}; {entry["address"]}\n')
    
  file.close()