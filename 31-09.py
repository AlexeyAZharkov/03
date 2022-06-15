class Circle:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x =x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def __setattr__(self, key, value):
        print(key)
        if type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'radius' and value <= 0:
            pass
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


circle = Circle(10.5, 72, 22)
circle.radius = -10 # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
x, y = circle.x, circle.y
res = circle.name # False, т.к. атрибут name не существует
print(circle.radius)
'''
 Объявите класс Circle (окружность), объекты которого должны создаваться командой:

circle = Circle(x, y, radius)   # x, y - координаты центра окружности; radius - радиус окружности

В каждом объекте класса Circle должны формироваться локальные приватные атрибуты:

__x, __y - координаты центра окружности (вещественные или целые числа);
__radius - радиус окружности (вещественное или целое положительное число).

Для доступа к этим приватным атрибутам в классе Circle следует объявить объекты-свойства (property):

x, y - для изменения и доступа к значениям __x, __y, соответственно;
radius - для изменения и доступа к значению __radius.

При изменении значений приватных атрибутов через объекты-свойства нужно дополнительно проверять, что присваиваемые 
значения - числа (целые или вещественные). Дополнительно у радиуса проверять, что число должно быть положительным 
(строго больше нуля). Сделать это нужно через магические методы. При некорректных переданных значениях, 
прежние значения меняться не должны.

Если присваиваемое значение не числовое, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")

При обращении к несуществующему атрибуту объектов класса Circle выдавать булево значение False.

Пример использования класса (эти строчки в программе писать не нужно):


'''