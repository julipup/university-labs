"""
Exercise 4. Write a program that requests the user to enter two numbers and
prints the sum, product, difference and quotient of the two numbers.

how many percent is the number 52 of the number 400.

"""

a = int(input("Number A: "))
b = int(input("Number B: "))

num_sum = a + b
num_difference = a - b
num_product = a * b

# Number Quotient
# a from b
num_quotient_1 = (a/b) * 100

# b from a
num_quotient_2 = (b/a) * 100

print("A + B =", num_sum)
print("A - B =", num_difference)
print("A * B =", num_product)
print("How many percent is the number A of the number B:", num_quotient_1)
print("...is the number B of the number A:", num_quotient_2)
