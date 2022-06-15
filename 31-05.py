class Shop:
    def __init__(self, name):
        self.name = name
        self.goods = []

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class Product:
    id_ = 1

    def __init__(self, name='', weight=0, price=0):
        self.id = Product.id_
        Product.id_ += 1
        print(self.id)
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'name' and type(value) != str:
            raise TypeError("Неверный тип присваиваемых данных.")
        elif (key == 'weight' or key == 'price') and type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif (key == 'weight' or key == 'price') and type(value) in (int, float) and value <= 0:
            raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)


shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 24)
shop.add_product(book)
shop.add_product(Product("Python", 150.5, 512))
# shop.remove_product(book)
shop.add_product(Product("Python1", 1502.5, 5122))
# del book.id
for p in shop.goods:
    print(f"{p.name}, {p.weight}, {p.price}, {p.id}")

'''
 Вы создаете интернет-магазин. Для этого нужно объявить два класса:

Shop - класс для управления магазином в целом;
Product - класс для представления отдельного товара.

Объекты класса Shop следует создавать командой:

shop = Shop(название магазина)

В каждом объекте класса Shop должно создаваться локальное свойство:

goods - список товаров (изначально список пустой).

А также в классе объявить методы:

add_product(self, product) - добавление нового товара в магазин (в конец списка goods);
remove_product(self, product) - удаление товара product из магазина (из списка goods);

Объекты класса Product следует создавать командой:

p = Product(название, вес, цена)

В них автоматически должны формироваться локальные атрибуты:

id - уникальный идентификационный номер товара (генерируется автоматически как целое положительное число от 1 и далее);
name - название товара (строка);
weight - вес товара (целое или вещественное положительное число);
price - цена (целое или вещественное положительное число).

В классе Product через магические методы (подумайте какие) осуществить проверку на тип присваиваемых 
данных локальным атрибутам объектов класса (например, id - целое число, name - строка и т.п.). Если проверка 
не проходит, то генерировать исключение командой:

raise TypeError("Неверный тип присваиваемых данных.")

Также в классе Product с помощью магического(их) метода(ов) запретить удаление локального атрибута id. При попытке 
это сделать генерировать исключение:

raise AttributeError("Атрибут id удалять запрещено.")

Пример использования классов (в программе эти строчки не писать):



'''