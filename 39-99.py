from random import choice


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2

    def __init__(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False

    @property
    def is_human_win(self):
        self.__check_game()
        return self.__is_human_win

    @is_human_win.setter
    def is_human_win(self, is_human_win):
        self.__is_human_win = is_human_win

    @property
    def is_computer_win(self):
        self.__check_game()
        return self.__is_computer_win

    @is_computer_win.setter
    def is_computer_win(self, is_computer_win):
        self.__is_computer_win = is_computer_win

    @property
    def is_draw(self):
        self.__check_game()
        return self.__is_draw

    @is_draw.setter
    def is_draw(self, is_draw):
        self.__is_draw = is_draw

    def __check_game(self):
        ls = self.pole
        all_pos = [[ls[i][j].value for j in range(3)] for i in range(3)]
        all_pos += [[ls[j][i].value for j in range(3)] for i in range(3)]
        all_pos.append([ls[0][0].value, ls[1][1].value, ls[2][2].value])
        all_pos.append([ls[0][2].value, ls[1][1].value, ls[2][0].value])
        for i in all_pos:
            if all(k == 2 for k in i):
                self.__is_computer_win = True
                return
            if all(k == 1 for k in i):
                self.__is_human_win = True
                return
        # self.__is_draw = True

    def __bool__(self):
        return not self.__is_human_win and not self.__is_computer_win \
               and any(self.pole[i][j] for i in range(3) for j in range(3))

    def init(self):
        self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
        self.is_human_win = False
        self.is_computer_win = False
        self.is_draw = False

    def show(self):
        for i in range(3):
            for j in range(3):
                print(self.pole[i][j].value, end=' ')
            print()

    def human_go(self):
        x, y = (int(i) - 1 for i in input('Ваш ход (строка, столбец, через пробел): ').split())
        self.__check_indx((x, y))
        if self.pole[x][y]:
            self.pole[x][y].value = self.HUMAN_X
        else:
            print('Клетка занята')

    def computer_go(self):
        lst = [self.pole[x][y] for x in range(3) for y in range(3) if self.pole[x][y]]
        choice(lst).value = self.COMPUTER_O

    def __getitem__(self, item):
        self.__check_indx(item)
        return self.pole[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.__check_indx(key)
        self.pole[key[0]][key[1]].value = value

    def __check_indx(self, i):
        if isinstance(i[0], int) and isinstance(i[1], int) and 0 <= i[0] < 3 and 0 <= i[1] < 3:
            return
        else:
            raise IndexError('некорректно указанные индексы')


class Cell:
    def __init__(self):
        self.value = 0

    def __bool__(self):
        return not bool(self.value)


game = TicTacToe()

print(game[1, 1]) # получение значения из клетки с индексами i, j
game[1, 1] = 2 # запись нового значения в клетку с индексами i, j
print(game[1, 1])
game.init()
# game.show()
game.human_go()
game.human_go()
game.human_go()
game.computer_go()
game.computer_go()
game.computer_go()


print(game.is_human_win)
game.show()
print('Игра нк окончена' if game else 'Game Over')
game.init()
print(game.is_draw)
print(game.is_human_win)
print(game.is_computer_win)
#
# game.init()
# step_game = 0
# while game:
#     game.show()
#
#     if step_game % 2 == 0:
#         game.human_go()
#     else:
#         game.computer_go()
#
#     step_game += 1
#
# game.show()
#
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")

'''
Необходимо объявить класс с именем TicTacToe (крестики-нолики) для управления игровым процессом. 
Объекты этого класса будут создаваться командой:

game = TicTacToe()

В каждом объекте этого класса должен быть публичный атрибут:

pole - двумерный кортеж, размером 3x3.

Каждый элемент кортежа pole является объектом класса Cell:

cell = Cell()

В объектах этого класса должно автоматически формироваться локальное свойство:

value - текущее значение в ячейке: 0 - клетка свободна; 1 - стоит крестик; 2 - стоит нолик.

Также с объектами класса Cell должна выполняться функция:

bool(cell) - возвращает True, если клетка свободна (value = 0) и False - в противном случае.

К каждой клетке игрового поля должен быть доступ через операторы:

res = game[i, j] # получение значения из клетки с индексами i, j
game[i, j] = value # запись нового значения в клетку с индексами i, j

Если индексы указаны неверно (не целые числа или числа, выходящие за диапазон [0; 2]), то следует генерировать исключение командой:

raise IndexError('некорректно указанные индексы')

Чтобы в программе не оперировать величинами: 0 - свободная клетка; 1 - крестики и 2 - нолики, в классе TicTacToe должны быть три публичных атрибута (атрибуты класса):

FREE_CELL = 0      # свободная клетка
HUMAN_X = 1        # крестик (игрок - человек)
COMPUTER_O = 2     # нолик (игрок - компьютер)

В самом классе TicTacToe должны быть объявлены следующие методы (как минимум):

init() - инициализация игры (очистка игрового поля, возможно, еще какие-либо действия);
show() - отображение текущего состояния игрового поля (как именно - на свое усмотрение);
human_go() - реализация хода игрока (запрашивает координаты свободной клетки и ставит туда крестик);
computer_go() - реализация хода компьютера (ставит случайным образом нолик в свободную клетку).

Также в классе TicTacToe должны быть следующие объекты-свойства (property):

is_human_win - возвращает True, если победил человек, иначе - False;
is_computer_win - возвращает True, если победил компьютер, иначе - False;
is_draw - возвращает True, если ничья, иначе - False.

Наконец, с объектами класса TicTacToe должна выполняться функция:

bool(game) - возвращает True, если игра не окончена (никто не победил и есть свободные клетки) и False - в противном случае.

Все эти функции и свойства предполагается использовать следующим образом (эти строчки в программе не писать):

game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")

Вам в программе необходимо объявить только два класса: TicTacToe и Cell так, чтобы с их помощью можно было бы сыграть 
в "Крестики-нолики" между человеком и компьютером.

P.S. Запускать игру и выводить что-либо на экран не нужно. Только объявить классы.

P.S.S. Домашнее задание: завершите создание этой игры и выиграйте у компьютера хотя бы один раз.
'''
