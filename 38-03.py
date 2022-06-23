class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        self.lst = list(self.__dict__)

    def __getitem__(self, item):
        if item >= len(self.lst) or not isinstance(item, int):
            raise IndexError('неверный индекс поля')
        return self.__dict__[self.lst[item]]

    def __setitem__(self, key, value):
        self.__dict__[self.lst[key]] = value



r = Record(pk=1, title='Python ООП', author='Балакирев')
print(r.title)
print(r[2])
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r.title)
print(r[1])
r[3] # генерируется исключение IndexError


'''
 Объявите класс Record (запись), который описывает одну произвольную запись из БД. Объекты этого класса создаются командой:

r = Record(field_name1=value1,... , field_nameN=valueN)

где field_nameX - наименование поля БД; valueX - значение поля из БД.

В каждом объекте класса Record должны автоматически создаваться локальные публичные атрибуты по именам полей 
(field_name1,... , field_nameN) с соответствующими значениями. Например:

r = Record(pk=1, title='Python ООП', author='Балакирев')

В объекте r появляются атрибуты:

r.pk # 1
r.title # Python ООП
r.author # Балакирев

Также необходимо обеспечить доступ к этим полям через индексы следующим образом:



Если указывается неверный индекс (не целое число или некорректное целое число), то должно генерироваться исключение командой:

raise IndexError('неверный индекс поля')

P.S. В программе нужно объявить только класс. Выводить на экран ничего не нужно.

P.P.S. Для создания локальных атрибутов используйте коллекцию __dict__ объекта класса Record.
'''