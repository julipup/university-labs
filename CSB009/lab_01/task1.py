# Створіть клас Rational для виконання арифметичних операцій з
# раціональними числами. Для ініціалізації атрибутів-даних
# класу - чисельника і знаменника - використовуйте метод
# __init__() з аргументами за замовчуванням для
# випадку, якщо початкові значення чисельника і знаменника
# не надані. Раціональне число в пам'яті повинно зберігатися
# в скороченій формі, наприклад, дріб 2/4 повинна зберігатися
# як 1 в чисельнику і 2 в знаменнику. Передбачити
# можливість виведення раціональних чисел у
# форматі a / b, де a - чисельник, b - знаменник і в форматі з плаваючою комою.
#
# Для демонстрації функціоналу класу Rational створіть консольний додаток.


class Rational:
    def __init__(self, a: float, b: float):
        # Saving numbers
        self.a = a
        self.b = b
        self.is_optimized = False

        # Trying to optimize saved numbers
        self.optimize_numbers()

    # Recursive function to optimize numbers
    # (it checks if we can divide numeral and
    # denominator by 2, 3 or 5)
    def optimize_numbers(self):
        def optimize(number):
            if number % 2 == 0:
                return 2
            elif number % 3 == 0:
                return 3
            elif number % 5 == 0:
                return 5

            return False

        if (optimize(self.a) and optimize(self.b)) and (optimize(self.a) == optimize(self.b)):
            self.a = self.a / optimize(self.a)
            self.b = self.b / optimize(self.b)

            # Trying to optimize this numbers even further
            self.optimize_numbers()
        else:
            self.is_optimized = True

    def to_str(self, print_as_float=True):
        if print_as_float:
            return self.a / self.b
        else:
            return f'{ self.a }/{ self.b }'

    def __str__(self):
        return f'Rational <a: { self.a }, b: { self.b }, is_optimized: { self.is_optimized }, float: { self.to_str() }>'


if __name__ == "__main__":
    # Console application
    print("Rational Number Tester\n")

    while True:
        a = float(input("| a = "))
        b = float(input("| b = "))

        # Building this number
        rational = Rational(a, b)

        # Printing this rational number
        print(rational, f'\n\nPrint as float: { rational.to_str() }\nPrint as a/b: { rational.to_str(False) }')

        if input("Continue? [Y/n] ").lower() == "n":
            exit()
