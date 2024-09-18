# Задание "Они все так похожи":
from math import pi


class Figure:
    sides_count = 0

    def __init__(self, color, list_sides):
        self.__sides = list_sides
        self.__color = color
        self.filled = True

    def set_color(self, *new_color):  # назначаем новый цвет
        self.__is_valid_color(new_color)
        if self.valid_color == True:
            self.__color = new_color

    def __is_valid_color(self, new_color):  # проверяем новый цвет
        self.valid_color = True
        for i in new_color:
            if not isinstance(i, int) or i < 0 or i > 255:
                self.valid_color = False
            return self.valid_color

    def get_color(self):  # предоставляет цвет
        return self.__color

    def set_sides(self, *new_sides):
        self.__is_valid_side(new_sides)
        if self.valid_sides == True:
            if len(new_sides) == self.sides_count:
                self.__sides = list(new_sides)

    def __is_valid_side(self, new_sides):  # проверка cторон фигуры
        self.valid_sides = True
        if len(new_sides) != len(self.__sides):
            self.valid_sides = False
            return self.valid_sides
        else:
            for i in new_sides:
                if not isinstance(i, int) or i < 0:
                    self.valid_sides = False
                    return self.valid_sides

    def get_sides(self):
        return self.__sides

    def __len__(self):              #надо вернуть периметр фигуры
        return self.__sides[0]      # Я думаю это не правильно


class Circle(Figure):
    sides_count = 1
    list_sides = []

    def __init__(self, color, long_side):
        self.__radius = long_side / (2 * pi)
        for i in range(self.sides_count):
            self.list_sides.append(long_side)
        super().__init__(color, self.list_sides)

    def get_square(self):
        return pi * self.__radius ** 2


class Cube(Figure):
    sides_count = 12
    list_sides = []

    def __init__(self, color, long_side):
        self.long_side = long_side
        for i in range(self.sides_count):
            self.list_sides.append(long_side)
        super().__init__(color, self.list_sides)

    def get_volume(self):
        return self.long_side ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, длина стороны/окружности)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))    # это я вообще не понимаю как его проверить!!!!

# Проверка объёма (куба):
print(cube1.get_volume())
