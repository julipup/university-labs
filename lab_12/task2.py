# б) Дан текстовий файл f. Записати в файл g зі збереженням порядку 
# проходження ті символи файлу f, яким в цьому файлі передує перше поєднання 'qwe'.

# Loading file
input_file = open('task2_input.txt', 'r')
parsed_string = ""

for line in input_file.readlines():
  buffer = []
  for symbol in list(line):
    if symbol in ['q', 'w', 'e']:
      buffer.append(symbol)
    else:
      if len(buffer) is 3:
        if ''.join(buffer) == 'qwe':
          # Adding this symbol to paresd string
          parsed_string += symbol

          # Emptying buffer
          buffer = []

print('Parsed string:', parsed_string)