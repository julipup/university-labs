# Task 2
# Написати програму на мові Python, яка обчислює значення функції
# y = 4x⌃3 - 2x⌃2 + 5 для значень x, що змінюються від -3 до 1, з кроком 0.1.


# Not universal function, that
def solve_problem(x: float):
    # Step 1:
    # 4x⌃3 as a
    a = 4 * x ** 3

    # Step 2:
    # 2x⌃2 as b
    b = 2 * x ** 2

    # Step 3:
    # a - b + 5
    return a - b + 5


# Solving math problem using not universal function
x = -3.0
while x < 1:
    x += 0.1
    print("x = {:.0f}, answer: {:.0f}".format(x, solve_problem(x)))
