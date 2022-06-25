class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.indx = -1
        self.table_lst = [[Cell(0) for _ in range(cols)] for _ in range(rows)]

    def __iter__(self):
        self.indx = -1
        return self

    def __next__(self):
        if self.indx < len(self.table_lst) - 1:
            self.indx += 1
        else:
            raise StopIteration
        return [i.data for i in self.table_lst[self.indx]]

    def __getitem__(self, item):
        return self.table_lst[item[0]][item[1]].data

    def __setitem__(self, key, value):
        self.table_lst[key[0]][key[1]].data = value


class Cell:
    def __init__(self, data):
        self.__data = data
        self.next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError('неверный тип присваиваемых данных')
        self.__data = data


table = TableValues(4, 3, type_data=int)
cell = Cell('data')

table[1, 2] = 2 # запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
table[2, 0] = 3
value = table[1, 2] # считывание значения из ячейки с индексами row, col
print(value)
print(table[1, 1])

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()


'''
 В программе необходимо реализовать таблицу TableValues по следующей схеме:

Сам класс TableValues представляет таблицу в целом, объекты которого создаются командой:

table = TableValues(rows, cols, type_data)

где rows, cols - число строк и столбцов таблицы; type_data - тип данных ячейки (int - по умолчанию, float, list, str 
и т.п.). Начальные значения в ячейках таблицы равны нулю (целое число).

Каждая ячейка таблицы должна быть представлена классом Cell. Объекты этого класса создаются командой:

cell = Cell(data)

где data - данные в ячейке. В каждом объекте класса Cell должен формироваться локальный приватный атрибут __data 
с соответствующим значением. Для работы с ним в классе Cell должно быть объект-свойство (property):

data - для записи и считывания информации из атрибута __data.

При попытке записать данные другого типа, должно генерироваться исключение командой:

raise TypeError('неверный тип присваиваемых данных')

С объектами класса TableValues должны выполняться следующие команды:

table[row, col] = value# запись нового значения в ячейку с индексами row, col (индексы отсчитываются с нуля)
value = table[row, col] # считывание значения из ячейки с индексами row, col

for row in table:  # перебор по строкам
    for value in row: # перебор по столбцам
        print(value, end=' ')  # вывод значений ячеек в консоль
    print()

При работе с индексами row, col, необходимо проверять их корректность. Если индексы не целое число или они 
выходят за диапазон размера таблицы, то генерировать исключение командой:

raise IndexError('неверный индекс')

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
'''