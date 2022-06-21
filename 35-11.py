class Box:
    def __init__(self):
        self.list_box = []

    def add_thing(self, obj):
        self.list_box.append(obj)

    def get_things(self):
        return self.list_box

    def __eq__(self, other):
        if len(self.list_box) != len(other.list_box):
            return False
        for th in self.list_box:
            if other.list_box.count(th) != 1:
                return False
        return True


class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.mass == other.mass


b1 = Box()
b2 = Box()

t1 = Thing('мел', 100)
t2 = Thing('тряпка', 200)
print(t1 == t2)
b1.add_thing(t1)
b1.add_thing(t2)
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))
# b2.add_thing(Thing('досsка', 2000))

res = b1 == b2 # True
print(res)

'''
Объявите в программе класс с именем Box (ящик), объекты которого должны создаваться командой:

box = Box()

А сам класс иметь следующие методы:

add_thing(self, obj) - добавление предмета obj (объект другого класса Thing) в ящик;
get_things(self) - получение списка объектов ящика.

Для описания предметов необходимо объявить еще один класс Thing. Объекты этого класса должны создаваться командой:

obj = Thing(name, mass)

где name - название предмета (строка); mass - масса предмета (число: целое или вещественное).
Объекты класса Thing должны поддерживать операторы сравнения:

obj1 == obj2
obj1 != obj2

Предметы считаются равными, если у них одинаковые названия name (без учета регистра) и массы mass.

Также объекты класса Box должны поддерживать аналогичные операторы сравнения:

box1 == box2
box1 != box2

Ящики считаются равными, если одинаковы их содержимое (для каждого объекта класса Thing одного ящика и можно 
найти ровно один равный объект из второго ящика).

Пример использования классов:



'''