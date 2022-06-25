class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.person_lst = [fio, job, old, salary, year_job]

    def __getitem__(self, item):
        if not isinstance(item, int) or not 0 <= item < 5:
            raise IndexError('неверный индекс')
        return self.person_lst[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or not 0 <= key < 5:
            raise IndexError('неверный индекс')
        self.person_lst[key] = value

    def __next__(self):
        for i in self.person_lst:
            return i


pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'

# print(pers[1])
# print(next(pers))
# print(next(pers))

for v in pers:
    print(v)
# pers[5] = 123 # IndexError

'''
Объявите в программе класс Person, объекты которого создаются командой:

p = Person(fio, job, old, salary, year_job)

где fio - ФИО сотрудника (строка); job - наименование должности (строка); old - возраст (целое число); 
salary - зарплата (число: целое или вещественное); year_job - непрерывный стаж на указанном месте работы (целое число).

В каждом объекте класса Person автоматически должны создаваться локальные атрибуты с такими же именами: 
fio, job, old, salary, year_job и соответствующими значениями.

Также с объектами класса Person должны поддерживаться следующие команды:

data = p[indx] # получение данных по порядковому номеру (indx) атрибута (порядок: fio, job, old, salary, year_job и начинается с нуля)
p[indx] = value # запись в поле с указанным индексом (indx) нового значения value
for v in p: # перебор всех атрибутов объекта в порядке: fio, job, old, salary, year_job
    print(v)

При работе с индексами, проверить корректность значения indx. Оно должно быть целым числом в диапазоне [0; 4]. 
Иначе, генерировать исключение командой:

raise IndexError('неверный индекс')

Пример использования класса (эти строчки в программе не писать):



P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.
'''