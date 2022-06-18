class Lib:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, book):
        self.book_list.remove(book)

    def pop_book(self, indx):
        self.book_list.pop(indx)

    def get_data(self):
        return [i for i in self.book_list]

    def __add__(self, other):
        self.add_book(other)
        return self

    def __sub__(self, other):
        if isinstance(other, Book):
            self.remove_book(other)
        elif isinstance(other, int):
            self.pop_book(other)
        return self

    def __len__(self):
        return len(self.book_list)


class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year


lib = Lib()
book = Book('title', 'author', 2222)
lib = lib + book # добавление новой книги в библиотеку
print(lib.get_data())
book1 = Book('title', 'author', 22)
lib += book1
lib += book
print(lib.get_data())

# lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

lib = lib - 1 # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
# lib -= 1
print(lib.get_data())
n = len(lib)
print(n)
'''
Вам поручается создать программу по учету книг (библиотеку). Для этого необходимо в программе объявить два класса:

Lib - для представления библиотеки в целом;
Book - для описания отдельной книги.

Объекты класса Book должны создаваться командой:

book = Book(title, author, year)

где title - заголовок книги (строка); author - автор книги (строка); year - год издания (целое число).

Объекты класса Lib создаются командой:

lib = Lib()

Каждый объект должен содержать локальный публичный атрибут:

book_list - ссылка на список из книг (объектов класса Book). Изначально список пустой.

Также объекты класса Lib должны работать со следующими операторами:

lib = lib + book # добавление новой книги в библиотеку
lib += book

lib = lib - book # удаление книги book из библиотеки (удаление происходит по ранее созданному объекту book класса Book)
lib -= book

lib = lib - indx # удаление книги по ее порядковому номеру (индексу: отсчет начинается с нуля)
lib -= indx

При реализации бинарных операторов + и - создавать копии библиотек (объекты класса Lib) не нужно.

Также с объектами класса Lib должна работать функция:

n = len(lib) # n - число книг

которая возвращает число книг в библиотеке.
'''