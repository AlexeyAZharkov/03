class Stack:
    def __init__(self):
        self.stack_lst = []
        self.top = None
        self.indx = -1

    def push_back(self, obj):
        self.stack_lst.append(obj)
        self.top = self.stack_lst[0]
        if len(self.stack_lst) > 1:
            self.stack_lst[-2].next = obj

    def push_front(self, obj):
        if not self.stack_lst:
            self.stack_lst.append(obj)
            self.top = self.stack_lst[0]
            return
        self.stack_lst.append(self.stack_lst[-1])
        for i in range(len(self.stack_lst) - 2, 0, -1):
            self.stack_lst[i] = self.stack_lst[i-1]
        self.stack_lst[0] = obj
        self.stack_lst[0].next = self.stack_lst[1]
        self.top = self.stack_lst[0]

    def __iter__(self):
        self.indx = -1
        return self

    def __next__(self):
        if self.indx < len(self.stack_lst) - 1:
            self.indx += 1
        else:
            raise StopIteration
        return self.stack_lst[self.indx]

    def __len__(self):
        return len(self.stack_lst)

    def __getitem__(self, item):
        if not isinstance(item, int) or not 0 <= item < len(self.stack_lst):
            raise IndexError('неверный индекс')
        return self.stack_lst[item].data

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not 0 <= key < len(self.stack_lst):
            raise IndexError('неверный индекс')
        self.stack_lst[key].data = value


class StackObj:
    def __init__(self, data):
        self.data = data
        self.next = None


st = Stack()
st.push_front(StackObj('00'))
st.push_back(StackObj('01'))
st.push_back(StackObj('02'))
st.push_back(StackObj('03'))

print('len(st)', len(st))
print('st[0]', st[0])
print('st[3]', st[3])
for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data, end=' ')
print()
st[2] = 'value' # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[2]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека
print('len(st)', len(st))

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data, end=' ')  # отображение данных в консоль

'''
Для этого, по прежнему, нужно объявить классы:

Stack - для представления стека в целом;
StackObj - для представления отдельных объектов стека.

В классе Stack должны быть методы:

push_back(obj) - для добавления нового объекта obj в конец стека;
push_front(obj) - для добавления нового объекта obj в начало стека.

В каждом объекте класса Stack должен быть публичный атрибут:

top - ссылка на первый объект стека (при пустом стеке top = None).

Объекты класса StackObj создаются командой:

obj = StackObj(data)

где data - данные, хранящиеся в объекте стека (строка).

Также в каждом объекте класса StackObj должны быть публичные атрибуты:

data - ссылка на данные объекта;
next - ссылка на следующий объект стека (если его нет, то next = None).

Наконец, с объектами класса Stack должны выполняться следующие команды:

st = Stack()

st[indx] = value # замена прежних данных на новые по порядковому индексу (indx); отсчет начинается с нуля
data = st[indx]  # получение данных из объекта стека по индексу
n = len(st) # получение общего числа объектов стека

for obj in st: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль

При работе с индексами (indx), нужно проверять их корректность. Должно быть целое число от 0 до N-1, 
где N - число объектов в стеке. Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')

P.S. В программе нужно объявить только классы. Выводить на экран ничего не нужно.
'''