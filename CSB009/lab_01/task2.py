# Створіть клас Rectangle. Для ініціалізації атрибутів-даних класу –
# довжини і ширини прямокутника – використовуйте метод __init__()
# з аргументами за замовчуванням. Передбачити можливість
# визначення периметра і площі прямокутника. Доступ до
# атрибутів-даних повинен бути контрольований (довжину
# і ширину прямокутника обмежити 100 см). Для демонстрації
# функціоналу класу Rectangle створіть консольний додаток.

class Rectangle:
    def __init__(self, width: float = 2, height: float = 2):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width: float):
        if new_width < 100:
            self.__width = new_width
        else:
            raise ValueError("Rectangle width can not be over 100")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height: float):
        if new_height < 100:
            self.__height = new_height
        else:
            raise ValueError("Rectangle height can not be over 100")

    def get_perimeter(self) -> float:
        return (self.__width + self.__width) * 2

    def get_area(self) -> float:
        return self.__width * self.__height

    def __str__(self):
        return f'Rectangle <height: { self.__height }, width: { self.__width }>'


if __name__ == "__main__":
    print("Rectangle Class Tester\n")

    while True:
        width = float(input("| width = "))
        height = float(input("| height = "))

        # Creating new Rectangle class
        rectangle = Rectangle(width, height)

        # Printing some information about this rectangle
        print(rectangle)
        print(f'Rectangle perimeter: { rectangle.get_perimeter() }\nRectangle area: { rectangle.get_area() }')

        if input("Continue? [Y/n] ").lower() == "n":
            exit()
