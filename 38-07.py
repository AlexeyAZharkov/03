class Stack:
    def __init__(self):
        self.top = None
        self.stack_lst = []

    def push(self, obj):
        self.stack_lst.append(obj)
        self.top = self.stack_lst[0]
        if len(self.stack_lst) > 1:
            self.stack_lst[-2].next = obj
        # print(len(self.stack_lst))

    def pop(self):
        p = self.stack_lst.pop()
        if len(self.stack_lst) == 0:
            self.top = None
        if len(self.stack_lst) > 0:
            self.stack_lst[-1].next = None
        # print(len(self.stack_lst))
        return p

    def __getitem__(self, item):
        if not isinstance(item, int) or item >= len(self.stack_lst):
            raise IndexError('неверный индекс')
        return self.stack_lst[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key >= len(self.stack_lst):
            raise IndexError('неверный индекс')
        self.stack_lst[key] = value


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st[1] = StackObj("new obj2")
print(st[2].data) # obj3
print(st[1].data) # new obj2
print(st.pop().data)   # исключение IndexError

'''
Для этого в программе объявлялись два класса: 

StackObj - для описания объектов стека;
Stack - для управления стек-подобной структурой.

И, далее, объекты класса StackObj следовало создавать командой:

obj = StackObj(data)

где data - это строка с некоторым содержимым объекта (данными). При этом каждый объект класса StackObj должен 
иметь следующие локальные атрибуты:

data - ссылка на строку с данными, указанными при создании объекта;
next - ссылка на следующий объект класса StackObj (при создании объекта принимает значение None).

Класс Stack предполагается использовать следующим образом:

st = Stack() # создание объекта стек-подобной структуры

В каждом объекте класса Stack должен быть локальный публичный атрибут:

top - ссылка на первый объект стека (если стек пуст, то top = None).

А в самом классе Stack следующие методы:

push(self, obj) - добавление объекта класса StackObj в конец стека;
pop(self) - извлечение последнего объекта с его удалением из стека;

Дополнительно в классе Stack нужно объявить магические методы для обращения к объекту стека по его индексу, например:

obj_top = st[0] # получение первого объекта
obj = st[4] # получение 5-го объекта стека
st[2] = StackObj("obj3") # замена прежнего (3-го) объекта стека на новый

Если индекс не целое число или число меньше нуля или больше числа объектов в стеке, то должно генерироваться исключение командой:

raise IndexError('неверный индекс')

Пример использования классов Stack и StackObj (эти строчки в программе не писать):



P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
'''