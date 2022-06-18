class Budget:
    def __init__(self):
        self.item_list = []

    def add_item(self, it):
        self.item_list.append(it)

    def remove_item(self, indx):
        self.item_list.pop(indx)

    def get_items(self):
        return self.item_list


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, Item):
            return self.money + other.money
        elif type(other) in (int, float):
            return self.money + other

    def __radd__(self, other):
        return self + other


my_budget = Budget()
it1 = Item("Курс по Python ООП", 2000)
it2 = Item("Курс по Django", 5000.01)
my_budget.add_item(it1)
my_budget.add_item(it2)
print(it1 + it2)
my_budget.add_item(Item("Курс по NumPy", 110))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x

print(s)

'''
Budget - для управления семейным бюджетом;
Item - пункт расходов бюджета.

Объекты класса Item должны создаваться командой:

it = Item(name, money)

где name - название статьи расхода; money - сумма расходов (вещественное или целое число).

Соответственно, в каждом объекте класса Item должны формироваться локальные атрибуты name и money с переданными 
значениями. Также с объектами класса Item должны выполняться, следующие операторы:

s = it1 + it2 # сумма для двух статей расходов

и в общем случае:

s = it1 + it2 + ... + itN # сумма N статей расходов

При суммировании оператор + должен возвращать число - вычисленную сумму 
по атрибутам money соответствующих объектов класса Item.

Объекты класса Budget создаются командой:

my_budget = Budget()

А сам класс Budget должен иметь следующие методы:

add_item(self, it) - добавление статьи расхода в бюджет (it - объект класса Item);
remove_item(self, indx) - удаление статьи расхода из бюджета по его порядковому номеру indx (индексу: отсчитывается с нуля);
get_items(self) - возвращает список всех статей расходов (список из объектов класса Item).

Пример использования классов (эти строчки в программе писать не нужно):



'''