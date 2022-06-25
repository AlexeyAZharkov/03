class TriangleListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i, self.j = 0, -1

    def __iter__(self):
        self.i, self.j = 0, -1
        return self

    def __next__(self):
        if self.j < self.i:
            self.j += 1
        elif self.i < len(self.lst) - 1:
            self.i += 1
            self.j = 0
        else:
            raise StopIteration
        return self.lst[self.i][self.j]


lst = [['x00'],
       ['x10', 'x11', 'x10', 'x11'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32', 'x33']]


it = TriangleListIterator(lst)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x, end=' ')
print()
it_iter = iter(it)
x = next(it_iter)
print(next(it_iter))
print(next(it_iter))

'''
Вам дают задание разработать итератор для последовательного перебора элементов вложенных (двумерных) списков следующей структуры:

lst = [[x00],
       [x10, x11],
       [x20, x21, x22],
       [x30, x31, x32, x33],
       ...
      ]

Для этого необходимо в программе объявить класс с именем TriangleListIterator, объекты которого создаются командой:

it = TriangleListIterator(lst)

где lst - ссылка на перебираемый список.

Затем, с объектами класса TriangleListIterator должны быть доступны следующие операции:

for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

it_iter = iter(it)
x = next(it_iter)

Итератор должен перебирать элементы списка по указанной треугольной форме. Даже если итератору на вход будет 
передан прямоугольная таблица (вложенный список), то ее перебор все равно должен осуществляться по треугольнику. 
Если же это невозможно (из-за структуры списка), то естественным образом должна возникать ошибка IndexError: 
index out of range (выход индекса за допустимый диапазон).

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
'''