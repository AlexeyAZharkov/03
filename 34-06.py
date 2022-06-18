class ListMath:
    def __init__(self, lst_math=[]):
        self.lst_math = self.normalise(lst_math)

    def normalise(self, lst):
        return [i for i in lst if type(i) in (int, float)]

    def get_list(self):
        return self.lst_math

    def __add__(self, other):
        res = [i + other for i in self.get_list()]
        return ListMath(res)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        for i in range(len(self.lst_math)):
            self.lst_math[i] += other
        return self

    def __sub__(self, other):
        res = [i - other for i in self.get_list()]
        return ListMath(res)

    def __rsub__(self, other):
        res = [-i for i in self.get_list()]
        return ListMath(res) + other

    def __isub__(self, other):
        for i in range(len(self.lst_math)):
            self.lst_math[i] -= other
        return self

    def __mul__(self, other):
        res = [i * other for i in self.get_list()]
        return ListMath(res)

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        for i in range(len(self.lst_math)):
            self.lst_math[i] *= other
        return self

    def __truediv__(self, other):
        res = [i / other for i in self.get_list()]
        return ListMath(res)

    def __itruediv__(self, other):
        for i in range(len(self.lst_math)):
            self.lst_math[i] /= other
        return self


lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]
print(lst.get_list(), id(lst))
lst = lst + 76 # сложение каждого числа списка с определенным числом
print(lst.get_list(), id(lst))
lst += 76.7  # сложение каждого числа списка с определенным числом
print(lst.get_list(), id(lst))
lst = lst - 76 # вычитание из каждого числа списка определенного числа
print(lst.get_list(), id(lst))
lst = 7.0 - lst # вычитание из каждого числа списка определенного числа
print(lst.get_list(), id(lst))
lst -= 76.3
print(lst.get_list(), id(lst))
lst = lst * 5 # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst.get_list(), id(lst))
lst = 5 * lst # умножение каждого числа списка на указанное число (в данном случае на 5)
print(lst.get_list(), id(lst))
lst *= 5.54
print(lst.get_list(), id(lst))
lst = lst / 13 # деление каждого числа списка на указанное число (в данном случае на 13)
print(lst.get_list(), id(lst))
lst /= 13.0
print(lst.get_list(), id(lst))

'''
Объявите класс с именем ListMath, объекты которого можно создавать командами:

lst1 = ListMath() # пустой список
lst2 = ListMath([1, 2, -5, 7.68]) # список с начальными значениями

В качестве значений элементов списка объекты класса ListMath должны отбирать только целые и вещественные числа, 
остальные игнорировать (если указываются в списке). Например:

lst = ListMath([1, "abc", -5, 7.68, True]) # ListMath: [1, -5, 7.68]

В каждом объекте класса ListMath должен быть публичный атрибут:

lst_math - ссылка на текущий список объекта (для каждого объекта создается свой список).

Также с объектами класса ListMath должны работать, следующие операторы:

При использовании бинарных операторов +, -, *, / должны формироваться новые объекты класса ListMath с новыми списками, 
прежние списки не меняются.

При использовании операторов +=, -=, *=, /= значения должны меняться внутри списка текущего объекта 
(новый объект не создается).

P.S. В программе достаточно только объявить класс. На экран ничего выводить не нужно. 
'''