import math


class Rectangle:
    def __init__(self, name: str, width: float, height: float):
        # Конструктор задаёт имя фигуры и её размеры (ширину и высоту)
        self.name = name
        self.width = width
        self.height = height

    # Одинаковое имя метода (print_formula) у разных классов — основа полиморфизма:
    # вызывающий код не заботится о том, какая именно фигура перед ним
    def print_formula(self):
        print("S = a * b")

    # Одинаковое имя метода (area) у разных классов: внутри каждого класса
    # площадь считается по своей формуле, но вызывается единообразно — shape.area()
    def area(self) -> float:
        return self.width * self.height


class Square:
    def __init__(self, name: str, side: float):
        self.name = name
        self.side = side

    def print_formula(self):
        print("S = a^2")

    def area(self) -> float:
        return self.side ** 2


class Circle:
    def __init__(self, name: str, radius: float):
        self.name = name
        self.radius = radius

    def print_formula(self):
        print("S = pi * r^2")

    def area(self) -> float:
        return math.pi * (self.radius ** 2)


# Создаём по 2 объекта каждого класса и складываем в один список
shapes = [
    Rectangle("Прямоугольник 1", 4, 5),
    Rectangle("Прямоугольник 2", 2.5, 6),
    Square("Квадрат 1", 3),
    Square("Квадрат 2", 7.5),
    Circle("Круг 1", 5),
    Circle("Круг 2", 2),
]

# Полиморфизм в действии: цикл проходит по разнородным объектам
# и вызывает у каждого одинаковые методы без ветвлений if/elif по типу объекта
for shape in shapes:
    shape.print_formula()
    print(f"{shape.name}: площадь = {shape.area():.2f}\n")