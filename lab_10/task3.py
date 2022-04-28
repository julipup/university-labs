# 3. Реалізуйте функцію, що виводить на екран прямокутник з зірочок «*». 
# Її параметрами будуть цілі числа, які описують довжину і ширину такого прямокутника.

def draw_rectangle(height = 4, width = 4):
  for row in range(0, height):
    line = ""

    for column in range(0, width):
      if row == 0 or row == height - 1:
        line += "*"
      else:
        if column == 0 or column == width - 1:
          line += "*"
        else:
          line += " "

    print(line)


# "Tests"
print("Height: 4, width: 4")
draw_rectangle()

print("Height 2, width: 2")
draw_rectangle(2, 2)

print("Height 2, width: 4")
draw_rectangle(2, 4)

print("Height 6, width: 12")
draw_rectangle(6, 12)
