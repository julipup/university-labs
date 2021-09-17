"""
Exercise 5. Write a program that reads in the radius of a circle and prints the
circle’s diameter, circumference and area. Use the constant
value 3.14159 for π. Do these calculations in output statements.
"""

pi = 3.14159

radius = float(input("Circle radius: "))
print("Circle diameter: {};\n"
      "Circle circumference: {};\n"
      "Circle Area: {};".format(radius * 2, 2 * radius * pi, pi * (radius ** 2)))
