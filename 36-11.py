class Triangle:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.check_triang()

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        if self.check_type(a):
            self.__a = a
            self.check_triang()

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        if self.check_type(b):
            self.__b = b
            self.check_triang()

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        if self.check_type(c):
            self.__c = c
            self.check_triang()

    def check_type(self, x):
        if type(x) in (int, float) and x > 0:
            return True
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

    def check_triang(self):
        if (self.__c < self.__a + self.__b) and (self.__a < self.__c + self.__b) and (self.__b < self.__c + self.__a):
            return True
        else:
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self):
        return self.__a + self.__b + self.__c

    def __call__(self, *args, **kwargs):
        p = len(self) / 2
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5


tr = Triangle(3, 1, 5)

print(len(tr))
# tr.b = 22
# tr.a = 1
print(tr())

'''
Объявите класс с именем Triangle, объекты которого создаются командой:

tr = Triangle(a, b, c)

где a, b, c - длины сторон треугольника (числа: целые или вещественные). В каждом объекте класса Triangle должны 
формироваться локальные приватные атрибуты:

__a, __b, __c - с соответствующими длинами сторон.

Для изменения и считывания информации из этих атрибутов, в классе Triangle объявите следующие объекты-свойства (property):

a, b, c - для изменения и считывания информации из атрибутов __a, __b, __c.

Также при записи нового значения в приватный атрибут (или в момент его создания) нужно проверять, 
что присваивается положительное число (целое или вещественное). Иначе, генерируется исключение командой:

raise ValueError("длины сторон треугольника должны быть положительными числами")

Также нужно проверять, что все три стороны a, b, c могут образовывать стороны треугольника. То есть, должны выполняться условия:

a < b+c; b < a+c; c < a+b

Иначе генерируется исключение командой:

raise ValueError("с указанными длинами нельзя образовать треугольник")

Наконец, с объектами класса Triangle должны выполняться функции:

len(tr) - возвращает периметр треугольника;
tr() - возвращает площадь треугольника (можно вычислить по формуле Герона: s = sqrt(p * (p-a) * (p-b) * (p-c)), где p - полупериметр треугольника).

P.S. На экран ничего выводить не нужно, только объявить класс Triangle.


def __setattr__(self, key, value):
        if not type(value) in (int, float) or value <= 0:
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        object.__setattr__(self, key, value)
        self.__check()

    def __check(self):
        if all(hasattr(self, name) for name in 'abc'):
            sides = [self.a, self.b, self.c]
            if max(sides) >= sum(sides) - max(sides):
                raise ValueError("с указанными длинами нельзя образовать треугольник")


    def __len__(self):
        return sum((self.a, self.b, self.c))

    def __call__(self):
        from functools import reduce
        p = len(self) / 2
        sides = [self.a, self.b, self.c]
        return reduce(lambda x, y: x * (p - y), sides, p)**0.5

'''