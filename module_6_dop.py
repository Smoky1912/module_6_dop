class Figure: # зададим класс Figure
    sides_count = 0  # атрибут класса Figure

    def __init__(self, color, *sides):   # зададим атрибуты класса
        self.filled = False  # по умолчанию объект не закрашен
        self.__color = self.__validate_color(color)  # список цветов в формате RGB
        self.__sides = self.__validate_sides(sides)  # список сторон (целые числа)

    def __validate_color(self, color):  # метод возвращает список RGB цветов
        if self.__is_valid_color(*color):  # валидация переданных знач.
            return color  # все ок? - возврат цвета
        else:  # иначе вернет список
            return [0, 0, 0]

    def __is_valid_color(self, r, g, b):  # проверка корректности переданных знач. цветов
        # проверка: целое ли значение и находится ли оно в диапазоне от 0 до 255
        # for c in [r, g, b] - проверяет условие для кажд. значения
        return all(isinstance(c, int) and 0 <= c <= 255 for c in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):  # если True - зн. цвета коррект.
            self.__color = [r, g, b]  # __color обновится

    def get_color(self):  # контролируемый доступ к __color
        return self.__color


    def __validate_sides(self, sides):
        if len(sides) != self.sides_count: # кол-во переданных сторон соот-ет ли ожидаемому
            return [1] * self.sides_count # нет - возврат список [1]
        elif self.__is_valid_sides(*sides): # целые положительные ли
            return list(sides) # список сторон
        else:  # иначе возврат списка [1]
            return [1] * self.sides_count

    def __is_valid_sides(self, *sides):
        # проверка: целое положительное ли и совпадает ли задан. кол-вом
        return all(isinstance(side, int) and side > 0 for side in sides)

    def get_sides(self): # метод должен возвращать значение я атрибута __sides
        return self.__sides

    def __len__(self):  # метод возврата периметра сторон - это сумма сторон
        return sum(self.__sides)

    def set_sides(self, *new_sides):  # принятие нов. сторон
        # если кол-во равно self.sides_count и  целое положительное ли
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides) # все ок? - обновл. знач. в список




import math  # нужен т.к. используется число Пи

class Circle(Figure): # зададим класс-наследник
    sides_count = 1   # атрибут класса

    def __init__(self, color, *sides): # зададим атрибуты класса
        super().__init__(color, *sides)   # вызов парам. родит. класса
        # self.__sides[0] - перв. эл. списка - длина окр-ти делен на 2 Пи
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self): #  метод возвращает длину окружности (пи на радиус в квадрате)
        return math.pi * (self.__radius ** 2)





class Triangle(Figure): # зададим класс-наследник
    sides_count = 3  # атрибут класса

    def __init__(self, color, *sides):  # вызов операторов родит. класса
        super().__init__(color, *sides)

    def get_square(self): # площадь тре-ника по формуле Герона
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))



class Cube(Figure): # зададим класс-наследник
    sides_count = 12 # атрибут класса

    def __init__(self, color, *sides):
        if len(sides) == 1: # проверим передана ли одна сторона
            # *(sides[0] for _ in range(12)) - список из 12ти знач. равных длинне одного ребра
            super().__init__(color, *(sides[0] for _ in range(12)))
        else: # если передано больше знач., то вызов констр. с парам. родит. класса
            super().__init__(color, *sides)

    def get_volume(self):  # возвращает объём куба
        side = self.get_sides()[0]  # извлекает первый эл. из списка ребер куба
        return side ** 3 # сторона в кубе

# Код для проверки:
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())