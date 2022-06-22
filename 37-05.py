import sys


class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self):
        return self.score > 0


lst_in = list(map(str.strip, sys.stdin.readlines()))

players = [Player(*line.split('; ')) for line in lst_in]

players_filtered = list(filter(bool, players))

# lst_in = ['Балакирев; 34; 2048', 'Mediel; 27; 0', 'Влад; 18; 9012', 'Nina P; 33; 0']

print(players_filtered)
print(bool(players[0]))
print(bool(players[1]))
print(bool(players_filtered[2]))

'''
Объявите в программе класс Player (игрок), объекты которого создаются командой:

player = Player(name, old, score)

где name - имя игрока (строка); old - возраст игрока (целое число); score - набранные очки в игре (целое число). 
В каждом объекте класса Player должны создаваться аналогичные локальные атрибуты: name, old, score.

С объектами класса Player должна работать функция:

bool(player)

которая возвращает True, если число очков больше нуля и False - в противном случае.

С помощью команды:

lst_in = list(map(str.strip, sys.stdin.readlines()))

считываются строки из входного потока в список строк lst_in. Каждая строка записана в формате:

"имя; возраст; очки"

Например:

Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0

Каждую строку списка lst_in необходимо представить в виде объекта класса Player с соответствующими данными. 
И из этих объектов сформировать список players.

Отфильтруйте этот список (создайте новый: players_filtered), оставив всех игроков с числом больше нуля. 
Используйте для этого стандартную функцию filter() совместно с функцией bool() языка Python. 

P.S. На экран ничего выводить не нужно.
'''