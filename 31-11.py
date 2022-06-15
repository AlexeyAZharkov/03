import time


class GeyserClassic:
    MAX_DATE_FILTER = 100
    filt_dict = {1: 'Mechanical', 2: 'Aragon', 3: 'Calcium'}

    def __init__(self):
        self.slots = {}

    def add_filter(self, slot_num, filter):
        if slot_num not in self.slots.keys() and self.filt_dict[slot_num] == filter.__class__.__name__:
            self.slots.update({slot_num: filter})

    def remove_filter(self, slot_num):
        self.slots.pop(slot_num)

    def get_filters(self):
        return tuple(self.slots.values())

    def water_on(self):
        if len(self.slots) == 3:
            for f in self.slots.values():
                if 0 > (time.time() - f.date) or self.MAX_DATE_FILTER < (time.time() - f.date):
                    return False
            return True
        return False


class Mechanical:
    def __init__(self, date):
        self.date = date


class Aragon:
    def __init__(self, date):
        self.date = date


class Calcium:
    def __init__(self, date):
        self.date = date



my_water = GeyserClassic()
my_water.add_filter(1, Mechanical(time.time()))
my_water.add_filter(2, Aragon(time.time()))
my_water.add_filter(2, Calcium(time.time()))
# my_water.remove_filter(2)
print(my_water.get_filters())
w = my_water.water_on() # False
print(w)
my_water.add_filter(3, Calcium(time.time()))
w = my_water.water_on() # True
print(w)
f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
print(my_water.get_filters())
print(f1, f3)
my_water.add_filter(3, Calcium(time.time())) # повторное добавление в занятый слот невозможно
my_water.add_filter(2, Calcium(time.time())) # добавление в "чужой" слот также невозможно
print(my_water.get_filters())
'''
 Объекты классов фильтров должны создаваться командами:

filter_1 = Mechanical(дата установки)
filter_2 = Aragon(дата установки)
filter_3 = Calcium(дата установки)

Во всех объектах этих классов должен формироваться локальный атрибут:

date - дата установки фильтров (для простоты - положительное вещественное число).

Также нужно запретить изменение этого атрибута после создания объектов этих классов (только чтение).

Объекты класса GeyserClassic должны создаваться командой:

g = GeyserClassic()

А сам класс иметь атрибут:

MAX_DATE_FILTER = 100 - максимальное время работы фильтра (любого)

и следующие методы:

add_filter(self, slot_num, filter) - добавление фильтра filter в указанный слот slot_num (номер слота: 1, 2 и 3), 
если он (слот) пустой (без фильтра). Также здесь следует проверять, что в первый слот можно установить только 
объекты класса Mechanical, во второй - объекты класса Aragon и в третий - объекты класса Calcium. 
Иначе, слот должен оставаться пустым.

remove_filter(self, slot_num) - извлечение фильтра из указанного слота (slot_num: 1, 2, и 3);

get_filters(self) - возвращает кортеж из набора трех фильтров в порядке их установки (по возрастанию номеров слотов);

water_on(self) - включение воды: возвращает True, если вода течет и False - в противном случае.

Метод water_on() должен возвращать значение True при выполнении следующих условий:

- все три фильтра установлены в слотах;
- все фильтры работают в пределах срока службы (значение (time.time() - date) должно быть в пределах [0; MAX_DATE_FILTER])

Пример использования классов  (эти строчки в программе писать не нужно):


'''