class LinkedList:
    def __init__(self):
        self.__list = []
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        self.__list.append(obj)
        self.head = self.__list[0]
        self.tail = self.__list[-1]
        if len(self.__list) > 1:
            obj.prev = self.__list[-2]

    def remove_obj(self, indx):
        self.__list.pop(indx)
        self.head = self.__list[0]
        self.tail = self.__list[-1]
        if 0 < indx < len(self.__list):
            self.__list[indx].prev = self.__list[indx - 1]
        if indx == 0:
            self.__list[0].prev = None
        if indx < len(self.__list):
            self.__list[indx - 1].next = self.__list[indx]
        if indx == len(self.__list):
            self.__list[indx - 1].next = None

    def __len__(self):
        return len(self.__list)

    def __call__(self, indx):
        return self.__list[indx]


class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    def __str__(self):
        return self.__data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, prev):
        self.__prev = prev

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(0)
linked_lst.add_obj(ObjList("Python ООП"))
print(len(linked_lst)) # n = 3
print(linked_lst(0)) # s = Balakirev


'''
Здесь создается список из связанных между собой объектов класса ObjList. Объекты этого класса создаются командой:

obj = ObjList(data)

где data - строка с некоторой информацией. Также в каждом объекте obj класса ObjList должны создаваться, следующие локальные атрибуты:

__data - ссылка на строку с данными;
__prev - ссылка на предыдущий объект связного списка (если объекта нет, то __prev = None);
__next - ссылка на следующий объект связного списка (если объекта нет, то __next = None).

В свою очередь, объекты класса LinkedList должны создаваться командой:

linked_lst = LinkedList()

и содержать локальные атрибуты:

head - ссылка на первый объект связного списка (если список пуст, то head = None);
tail - ссылка на последний объект связного списка (если список пуст, то tail = None).

А сам класс содержать следующие методы:

add_obj(obj) - добавление нового объекта obj класса ObjList в конец связного списка;
remove_obj(indx) - удаление объекта класса ObjList из связного списка по его порядковому номеру (индексу); 
индекс отсчитывается с нуля.

Также с объектами класса LinkedList должны поддерживаться следующие операции:

len(linked_lst) - возвращает число объектов в связном списке;
linked_lst(indx) - возвращает строку __data, хранящуюся в объекте класса ObjList, расположенного под индексом 
indx (в связном списке).

Пример использования классов (эти строчки в программе писать не нужно):



P.S. На экран в программе ничего выводить не нужно. 
'''