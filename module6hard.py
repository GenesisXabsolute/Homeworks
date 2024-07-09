from math import sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides, filled=None):
        if type(self) is Cube:
            self.__sides = [sides[0] for _ in range(12)]
        else:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return r <= 255 and g <= 255 and b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides.clear()
            self.__sides.extend(new_sides)

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *n):
        return all([type(i) is int and i >= 0 for i in n]) and len(n) == len(self.__sides)

    def __len__(self):
        pass


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            sides = 1
            super().__init__(color, 1)
        else:
            super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / 6.28

    def get_square(self):
        return self.__radius ** 2 * 3.14

    def __len__(self):
        a = sum(self.get_sides())
        return a


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        if len(sides) != self.sides_count:
            super().__init__(color, 1, 1, 1)
        else:
            super().__init__(color, *sides)
        self.__height = (self.get_square() / self.get_sides()[1]) * 2

    def get_square(self):
        s = sum(self.get_sides()) / 2
        c1 = self.get_sides()[0]
        c2 = self.get_sides()[1]
        c3 = self.get_sides()[2]
        return sqrt(s * (s - c1) * (s - c2) * (s - c3))  # Формула Герона'


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) != 1:
            super().__init__(color, 1)
        else:
            a = sides[0]
            super().__init__(color, a)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # Не изменится
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
circle1.set_sides(15)  # Изменится
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
