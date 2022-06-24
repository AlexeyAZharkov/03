class TicTacToe:
    def __init__(self):
        self.pole = tuple()
        for i in range(3):
            self.pole += (tuple(Cell() for _ in range(3)),)

    def clear(self):
        for i in range(3):
            for j in range(3):
                self.pole[i][j].value = 0
                self.pole[i][j].is_free = True

    def __getitem__(self, item):
        if isinstance(item[0], slice):
            return self.pole[0][item[1]].value, self.pole[1][item[1]].value, self.pole[2][item[1]].value
        if isinstance(item[1], slice):
            return tuple(i.value for i in self.pole[item[0]][item[1]])
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        if 0 > key[0] or 2 < key[0] or 2 < key[1] or 0 > key[1]:
            raise IndexError('неверный индекс клетки')
        if not self.pole[key[0]][key[1]]:
            raise ValueError('клетка уже занята')
        self.pole[key[0]][key[1]].value = value
        self.pole[key[0]][key[1]].is_free = False


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free



game = TicTacToe()
# print(game.pole)
game.clear()

game[0, 0] = 1
game[1, 0] = 2
# формируется поле:
# 1 0 0
# 2 0 0
# 0 0 0
# game[3, 2] = 2 # генерируется исключение IndexError
if game[0, 0] == 0:
    game[0, 0] = 2
print(game[1, 0])
print(game[0, 0])
print(game[:, 0])  # 1, 2, 0
print(game[0, :])  # 1, 0, 0
print(game[1, 0])
# print(game.pole)

# print(game.pole)

'''
Вам нужно реализовать в программе игровое поле для игры "Крестики-нолики". Для этого требуется объявить 
класс TicTacToe (крестики-нолики), объекты которого создаются командой:

game = TicTacToe()

Каждый объект game должен иметь публичный атрибут:

pole - игровое поле: кортеж размером 3х3 с объектами класса Cell.

Каждая клетка игрового поля представляется объектом класса Cell и создается командой:

cell = Cell()

Объекты класса Cell должны иметь следующие публичные локальные атрибуты:

is_free - True, если клетка свобода; False - в противном случае;
value - значение поля: 1 - крестик; 2 - нолик (по умолчанию 0).

Также с каждым объектом класса Cell должна работать функция:

bool(cell)

которая возвращает True, если клетка свободна (cell.is_free=True) и False - в противном случае.

Класс TicTacToe должен иметь следующий метод:

clear() - очистка игрового поля (все клетки заполняются нулями и переводятся в закрытое состояние);

А объекты этого класса должны иметь следующую функциональность (обращение по индексам):

game[0, 0] = 1 # установка нового значения, если поле закрыто
res = game[1, 1] # получение значения центральной ячейки поля (возвращается число)

Если указываются некорректные индексы, то должно генерироваться исключение командой:

raise IndexError('неверный индекс клетки')

Если идет попытка присвоить новое значение в открытую клетку поля, то генерировать исключение:

raise ValueError('клетка уже занята')

Также должны быть реализованы следующие срезы при обращении к клеткам игрового поля:

slice_1 = game[:, indx] # выбираются все элементы (кортеж) столбца с индексом indx
slice_2 = game[indx, :] # выбираются все элементы (кортеж) строки с индексом indx

Пример использования классов (эти строчки в программе не писать):



P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.

P.P.S. При передаче среза в магических методах __setitem__() и __getitem__() параметр индекса становится объектом 
класса slice. Его можно указывать непосредственно в квадратных скобках упорядоченных коллекций (списков, кортежей и т.п.).
'''