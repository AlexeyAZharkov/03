class Matrix:
    def __init__(self, *args):
        if isinstance(args[0], list):
            self.check_matrix2d(args[0])
            self.matrix = args[0]
            self.rows = len(self.matrix)
            self.cols = len(self.matrix[0])
        else:
            self.rows, self.cols, self.fill_value = args
            if type(self.fill_value) not in (int, float) or not isinstance(self.rows, int) or not isinstance(self.cols, int):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.matrix = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]

    def check_matrix2d(self, m):
        for i in range(len(m)):
            if len(m[0]) != len(m[i]):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            for j in range(len(m)):
                if type(m[i][j]) not in (int, float):
                    raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def __getitem__(self, item):
        self.check_indx(item)
        return self.matrix[item[0]][item[1]]

    def __setitem__(self, key, value):
        self.check_indx(key)
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')
        self.matrix[key[0]][key[1]] = value

    def check_indx(self, item):
        if not isinstance(item[0], int) or not isinstance(item[1], int) or 0 > item[0] or 0 > item[1] \
                or item[0] >= self.rows or item[1] >= self.cols:
            raise IndexError('недопустимые значения индексов')

    def __add__(self, other):
        if type(other) == Matrix:
            if self.cols == other.cols and self.rows == other.rows:
                m = [[self.matrix[j][i] + other.matrix[j][i] for i in range(self.cols)] for j in range(self.rows)]
            else:
                raise ValueError('операции возможны только с матрицами равных размеров')
        elif type(other) in (int, float):
            m = [[self.matrix[j][i] + other for i in range(self.cols)] for j in range(self.rows)]
        return Matrix(m)

    def __sub__(self, other):
        if type(other) == Matrix:
            if self.cols == other.cols and self.rows == other.rows:
                m = [[self.matrix[j][i] - other.matrix[j][i] for i in range(self.cols)] for j in range(self.rows)]
            else:
                raise ValueError('операции возможны только с матрицами равных размеров')
        elif type(other) in (int, float):
            m = [[self.matrix[j][i] - other for i in range(self.cols)] for j in range(self.rows)]
        return Matrix(m)


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 2], [3, 4]])
print(m1[0, 0]) # 1
print(m1[0, 1]) # 2
print(m1[1, 0]) # 3
print(m1[1, 1]) # 4

matrix = Matrix(4, 5, 0)
print(matrix[0, 0]) # возвращается первый элемент матрицы
matrix[1, 2] = 3 # элементу матрицы с индексами (indx1, indx2) присваивается новое значение
print(matrix[1, 2])
print()
matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
# matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
print(matrix[1, 0])
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
# matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1
print(matrix[1, 0])

'''
 Объявите класс Matrix (матрица) для операций с матрицами. Объекты этого класса должны создаваться командой:

m1 = Matrix(rows, cols, fill_value)

где rows, cols - число строк и столбцов матрицы; fill_value - заполняемое начальное значение элементов матрицы 
(должно быть число: целое или вещественное). Если в качестве аргументов передаются не числа, то генерировать исключение:

raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

Также объекты можно создавать командой:

m2 = Matrix(list2D)

где list2D - двумерный список (прямоугольный), состоящий из чисел (целых или вещественных). Если список list2D 
не прямоугольный, или хотя бы один из его элементов не число, то генерировать исключение командой:

raise TypeError('список должен быть прямоугольным, состоящим из чисел')

Для объектов класса Matrix должны выполняться следующие команды:

matrix = Matrix(4, 5, 0)
res = matrix[0, 0] # возвращается первый элемент матрицы
matrix[indx1, indx2] = value # элементу матрицы с индексами (indx1, indx2) присваивается новое значение

Если в результате присвоения тип данных не соответствует числу, то генерировать исключение командой:

raise TypeError('значения матрицы должны быть числами')

Если указываются недопустимые индексы матрицы (должны быть целыми числами от 0 и до размеров матрицы), то генерировать исключение:

raise IndexError('недопустимые значения индексов')

Также с объектами класса Matrix должны выполняться операторы:

matrix = m1 + m2 # сложение соответствующих значений элементов матриц m1 и m2
matrix = m1 + 10 # прибавление числа ко всем элементам матрицы m1
matrix = m1 - m2 # вычитание соответствующих значений элементов матриц m1 и m2
matrix = m1 - 10 # вычитание числа из всех элементов матрицы m1

Во всех этих операция должна формироваться новая матрица с соответствующими значениями. Если размеры матриц 
не совпадают (разные хотя бы по одной оси), то генерировать исключение командой:

raise ValueError('операции возможны только с матрицами равных размеров')

Пример для понимания использования индексов (эти строчки в программе писать не нужно):

mt = Matrix([[1, 2], [3, 4]])
res = mt[0, 0] # 1
res = mt[0, 1] # 2
res = mt[1, 0] # 3
res = mt[1, 1] # 4

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
'''