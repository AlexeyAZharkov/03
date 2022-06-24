class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table_dict = {}

    def add_data(self, row, col, data):
        if not isinstance(row, int) or not isinstance(col, int) or row < 0 or col < 0:
            raise IndexError('неверный индекс, должен быть положительное целое число')
        self.table_dict.update({(row, col): data})
        self.rows = max(i[0] for i in self.table_dict.keys()) + 1
        self.cols = max(i[1] for i in self.table_dict.keys()) + 1

    def remove_data(self, row, col):
        if not isinstance(row, int) or not isinstance(col, int) or row < 0 or col < 0:
            raise IndexError('неверный индекс, должен быть положительное целое число')
        if (row, col) not in self.table_dict.keys():
            raise IndexError('ячейка с указанными индексами не существует')
        self.table_dict.pop((row, col))
        self.rows = max(i[0] for i in self.table_dict.keys()) + 1
        self.cols = max(i[1] for i in self.table_dict.keys()) + 1

    def __getitem__(self, item):
        if not isinstance(item[0], int) or not isinstance(item[1], int) or item[0] < 0 or item[1] < 0:
            raise IndexError('неверный индекс, должен быть положительное целое число')
        if (item[0], item[1]) not in self.table_dict.keys():
            raise ValueError('данные по указанным индексам отсутствуют')
        return self.table_dict[(item[0], item[1])].value

    def __setitem__(self, key, value):
        if not isinstance(key[0], int) or not isinstance(key[1], int) or key[0] < 0 or key[1] < 0:
            raise IndexError('неверный индекс, должен быть положительное целое число')
        self.add_data(key[0], key[1], Cell(value))


class Cell:
    def __init__(self, value):
        self.value = value


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
st.add_data(0, 0, Cell("cell_00"))
st[2, 5] = 25 # изменение значения существующей ячейки
print(st.rows, st.cols)
st[11, 7] = 'cell_117' # создание новой ячейки
st[11, 7] = 'cell_117'
print(st[0, 0]) # cell_00
print(st[2, 5]) # cell_00
print(st[11, 7])
# st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
st.remove_data(11, 7)
print(st.rows, st.cols)
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError

'''
 Вам необходимо описывать в программе очень большие и разреженные таблицы данных (с большим числом пропусков). 
 Для этого предлагается объявить класс SparseTable, объекты которого создаются командой:

st = SparseTable()

В каждом объекте этого класса должны создаваться локальные публичные атрибуты:

rows - общее число строк таблицы (начальное значение 0);
cols - общее число столбцов таблицы (начальное значение 0).

В самом классе SparseTable должны быть объявлены методы:

add_data(row, col, data) - добавление данных data (объект класса Cell) в таблицу по индексам row, col (целые неотрицательные числа);
remove_data(row, col) - удаление ячейки (объект класса Cell) с индексами (row, col).

При удалении/добавлении новой ячейки должны автоматически пересчитываться атрибуты rows, cols объекта класса SparseTable. 
Если происходит попытка удалить несуществующую ячейку, то должно генерироваться исключение:

raise IndexError('ячейка с указанными индексами не существует')

Ячейки таблицы представляют собой объекты класса Cell, которые создаются командой:

data = Cell(value)

где value - данные ячейки (любой тип).

Хранить ячейки следует в словаре, ключами которого являются индексы (кортеж) i, j, а значениями - объекты класса Cell.

Также с объектами класса SparseTable должны выполняться команды:

res = st[i, j] # получение данных из таблицы по индексам (i, j)
st[i, j] = value # запись новых данных по индексам (i, j)

Чтение данных возможно только для существующих ячеек. Если ячейки с указанными индексами нет, то генерировать исключение командой:

raise ValueError('данные по указанным индексам отсутствуют')

При записи новых значений их следует менять в существующей ячейке или добавлять новую, если ячейка с индексами (i, j) 
отсутствует в таблице. (Не забывайте при этом пересчитывать атрибуты rows и cols).

Пример использования классов (эти строчки в программе не писать):



P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
'''