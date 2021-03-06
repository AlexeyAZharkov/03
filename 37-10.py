class Vector:
    def __init__(self, *args):
        self.coords = list(args)

    def __add__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        t = (x + other.coords[i] for i, x in enumerate(self.coords))
        return Vector(*t)

    def __iadd__(self, other):
        for i in range(len(self.coords)):
            self.coords[i] += other
        return self

    def __sub__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        t = (x - other.coords[i] for i, x in enumerate(self.coords))
        return Vector(*t)

    def __isub__(self, other):
        for i in range(len(self.coords)):
            self.coords[i] -= other
        return self

    def __mul__(self, other):
        if len(self.coords) != len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')
        t = (x * other.coords[i] for i, x in enumerate(self.coords))
        return Vector(*t)

    def __eq__(self, other):
        if len(self.coords) != len(other.coords):
            return False
        return all(x == other.coords[i] for i, x in enumerate(self.coords))

    def __repr__(self):
        return str(self.coords[0])


v1 = Vector(1, 2, 3)
v2 = Vector(4, 2, 3)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 != v2)
v1 += 10
print(v1)
v1 -= 13
print(v1)


# print(bool(el2))
# print(el2.get_coords())

'''
Объявите в программе класс Vector, объекты которого создаются командой:

v = Vector(x1, x2, x3,..., xN)

где x1, x2, x3,..., xN - координаты вектора (числа: целые или вещественные).

С каждым объектом класса Vector должны выполняться операторы:

v1 + v2 # суммирование соответствующих координат векторов
v1 - v2 # вычитание соответствующих координат векторов
v1 * v2 # умножение соответствующих координат векторов

v1 += 10 # прибавление ко всем координатам вектора числа 10
v1 -= 10 # вычитание из всех координат вектора числа 10

v1 == v2 # True, если соответствующие координаты векторов равны
v1 != v2 # True, если хотя бы одна пара координат векторов не совпадает

При реализации бинарных операторов +, -, * следует создавать новые объекты класса Vector с новыми (вычисленными) 
координатами. При реализации операторов +=, -= координаты меняются в текущем объекте, не создавая новый.

Если число координат (размерность) векторов v1 и v2 не совпадает, то при операторах +, -, * должно генерироваться исключение командой:

raise ArithmeticError('размерности векторов не совпадают')

P.S. В программе на экран выводить ничего не нужно, только объявить класс.
'''