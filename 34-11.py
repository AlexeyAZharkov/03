class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        self.check_matrix(matrix)
        return self.step_2(self.step_1(matrix))

    def step_1(self, m):
        matrix1 = []
        for k in range(len(m)):
            line1 = []
            for i in range(0, len(m[0]), self.step[0]):
                if i + self.size[0] <= len(m[0]):
                    line1.append(max([m[k][j] for j in range(i, i + self.size[0])]))
            matrix1.append(line1)
        return matrix1

    def step_2(self, m):
        matrix1 = []

        for k in range(len(m[0])):
            row = []
            for i in range(0, len(m), self.step[1]):
                if i + self.size[1] <= len(m):
                    row.append(max([m[j][k] for j in range(i, i + self.size[1])]))
            matrix1.append(row)
        line = []
        res_m = []
        for i in range(len(matrix1[0])):
            line.append([matrix1[j][i] for j in range(len(matrix1))])
        res_m.extend(line)
        return res_m

    def check_matrix(self, matrix):
        if self.get_depth(matrix) != 2:
            raise ValueError("Неверный формат для первого параметра matrix.")
        len_x = len(matrix)
        len_y = len(matrix[0])
        for i in range(len_x):
            if len(matrix[i]) != len_y:
                raise ValueError("Неверный формат для первого параметра matrix.")
            for j in range(len_y):
                if type(matrix[i][j]) not in (int, float):
                    raise ValueError("Неверный формат для первого параметра matrix.")

    def get_depth(self, l):
        if isinstance(l, (list, tuple)):
            t = []
            for itm in l:
                t += self.get_depth(itm),
            return 1 + (max(t) if t else 0)
        return 0


mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2], [5, 4, 3, 2], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
print(res)

'''
Мы повторим эту процедуру. Для этого в программе нужно объявить класс с именем MaxPooling, объекты которого создаются командой:

mp = MaxPooling(step=(2, 2), size=(2,2))

где step - шаг смещения окна по горизонтали и вертикали; size - размер окна по горизонтали и вертикали.

Параметры step и size по умолчанию должны принимать кортеж со значениями (2, 2).

Для выполнения операции Max Pooling используется команда:

res = mp(matrix)

где matrix - прямоугольная таблица чисел; res - ссылка на результат обработки таблицы matrix (должна создаваться новая 
таблица чисел.

Прямоугольную таблицу чисел следует описывать вложенными списками. Если при сканировании таблицы часть окна выходит 
за ее пределы, то эти данные отбрасывать (не учитывать все окно).

Если matrix не является прямоугольной таблицей или содержит хотя бы одно не числовое значение, 
то должно генерироваться исключение командой:

raise ValueError("Неверный формат для первого параметра matrix.")

Пример использования класса (эти строчки в программе писать не нужно):

mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2], [5, 6, 7, 8], [5, 11, 7, 8]])    # [[6, 8], [9, 7]]

Результатом будет таблица чисел:

6 8
9 7
'''