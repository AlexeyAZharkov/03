class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.lst = []

    def add_point(self, x, y, speed):
        self.lst.append([x, y, speed])

    def __getitem__(self, item):
        if item >= len(self.lst) or not isinstance(item, int):
            raise IndexError('некорректный индекс')
        return (self.lst[item][0], self.lst[item][1]), self.lst[item][2]

    def __setitem__(self, key, value):
        self.lst[key][2] = value


tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

c, s = tr[2]
print(c, s)
tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError

'''
Вам необходимо для навигатора реализовать определение маршрутов. Для этого в программе нужно объявить класс Track,
 объекты которого создаются командой:

tr = Track(start_x, start_y)

где start_x, start_y - координата начала пути.

В этом классе должен быть реализован следующий метод:

add_point(x, y, speed) - добавление новой точки маршрута (линейный сегмент), который можно пройти со средней скоростью speed.

Также с объектами класса Track должны выполняться команды:

coord, speed = tr[indx] # получение координаты (кортеж с двумя числами) и скорости (число) для линейного сегмента 
маршрута с индексом indx
tr[indx] = speed # изменение средней скорости линейного участка маршрута по индексу indx

Если индекс (indx) указан некорректно (должен быть целым числом от 0 до N-1, где N - число линейных сегментов 
в маршруте), то генерируется исключение командой:

raise IndexError('некорректный индекс')

Пример использования класса (эти строчки в программе не писать):

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2

tr[2] = 60
c, s = tr[2]
print(c, s)

res = tr[3] # IndexError

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
'''