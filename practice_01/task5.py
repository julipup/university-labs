"""
Exercise 5. Write a program that reads in the radius of a circle and prints the
circle’s diameter, circumference and area. Use the constant
value 3.14159 for π. Do these calculations in output statements.
"""

pi = 3.14159

radius = float(input("Circle radius: "))
diameter = radius * 2
circumference = 2 * radius * pi
area = pi * (radius ** 2)

print("Circle diameter:", diameter)
print("Circle circumference:", circumference)
print("Circle area:", area)
