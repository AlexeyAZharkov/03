class Stack:
    def __init__(self):
        self.lst_st = []
        self.top = None

    def push_back(self, obj):
        self.lst_st.append(obj)
        self.top = self.lst_st[0]
        if len(self.lst_st) > 1:
            self.lst_st[-2].next = obj

    def pop_back(self):
        self.lst_st.pop()
        if len(self.lst_st) == 0:
            self.top = None
        if len(self.lst_st) > 0:
            self.lst_st[-1].next = None

    def get_data(self):
        return [(i.data, i.next) for i in self.lst_st]

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for data in other:
            self.push_back(StackObj(data))
        return self


class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next



st = Stack()
print(st)
print(st.get_data())
# добавление нового объекта класса StackObj в конец стека st
obj = StackObj('data')
st = st + obj
st += obj
print(st.get_data())
# добавление нескольких объектов в конец стека
st = st * ['data_1', 'data_2', 'data_N']
st *= ['data_1', 'data_2', 'data_N']
print(st.get_data())
'''
Давайте снова создадим такую структуру данных. Для этого объявим два класса:

Stack - для управления стеком в целом;
StackObj - для представления отдельных объектов в стеке.

Объекты класса StackObj должны создаваться командой:

obj = StackObj(data)

где data - строка с некоторыми данными.

Каждый объект класса StackObj должен иметь локальные приватные атрибуты:

__data - ссылка на строку с переданными данными;
__next - ссылка на следующий объект стека (если следующего нет, то __next = None).

Объекты класса Stack создаются командой:

st = Stack()

и каждый из них должен содержать локальный атрибут:

top - ссылка на первый объект стека (если объектов нет, то top = None).

Также в классе Stack следует объявить, следующие методы:

push_back(self, obj) - добавление объекта класса StackObj в конец стека;
pop_back(self) - удаление последнего объекта из стека.

Дополнительно нужно реализовать, следующий функционал:

# добавление нового объекта класса StackObj в конец стека st
st = st + obj 
st += obj

# добавление нескольких объектов в конец стека
st = st * ['data_1', 'data_2', ..., 'data_N']
st *= ['data_1', 'data_2', ..., 'data_N']

В последних двух строчках должны автоматически создаваться N объектов класса StackObj с данными, взятыми 
из списка (каждый элемент списка для очередного добавляемого объекта).
'''