class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.bag_lst = []

    def add_thing(self, thing):
        if sum(t.weight for t in self.bag_lst) + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.bag_lst.append(thing)

    def __getitem__(self, item):
        if not isinstance(item, int) or item >= len(self.bag_lst):
            raise IndexError('неверный индекс')
        return self.bag_lst[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key >= len(self.bag_lst):
            raise IndexError('неверный индекс')
        if sum(t.weight for t in self.bag_lst) - self.bag_lst[key].weight + value.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')
        self.bag_lst[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int) or key >= len(self.bag_lst):
            raise IndexError('неверный индекс')
        del self.bag_lst[key]


class Thing:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 500))
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 1000)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
# t = bag[4] # генерируется исключение IndexError

'''
Объявите в программе класс Bag (сумка), объекты которого создаются командой:

bag = Bag(max_weight)

где max_weight - максимальный суммарный вес предметов, который можно положить в сумку.

Каждый предмет описывается классом Thing и создается командой:

t = Thing(name, weight)

где name - название предмета (строка); weight - вес предмета (вещественное или целочисленное значение). В объектах 
класса Thing должны автоматически формироваться локальные свойства с теми же именами: name и weight.

В классе Bag должен быть реализован метод:

add_thing(thing) - добавление нового объекта thing класса Thing в сумку.

Добавление выполняется только если суммарный вес вещей не превышает параметра max_weight. Иначе, генерируется исключение:

raise ValueError('превышен суммарный вес предметов')

Также с объектами класса Bag должны выполняться следующие команды:

t = bag[indx] # получение объекта класса Thing по индексу indx (в порядке добавления вещей, начиная с 0)
bag[indx] = t # замена прежней вещи на новую t, расположенной по индексу indx
del bag[indx] # удаление вещи из сумки, расположенной по индексу indx

Если индекс в этих командах указывается неверно, то должно генерироваться исключение:

raise IndexError('неверный индекс')

Пример использования классов (эти строчки в программе не писать):



P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
'''