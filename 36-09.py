import sys

class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = int(year)

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return self.name.lower() == other.name.lower() and self.author.lower() == other.author.lower()


lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_bs = [BookStudy(*line.split('; ')) for line in lst_in]

unique_books = len(set(lst_bs))

print(unique_books)

# lst_in = ['Python; Балакирев С.М.; 2020', 'Python1 ООП; Балакирев С.М.; 2021', 'Python ООП; Балакирев С.М.; 2022',
#           'Python; Балакирев2 С.М.; 2021']


'''
Из входного потока необходимо прочитать список строк командой:

lst_in = list(map(str.strip, sys.stdin.readlines()))

Каждая строка содержит информацию об учебном пособии в формате:

"Название; автор; год издания"

Например:

Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021

Необходимо каждую из этих строк представить объектом класса BookStudy, которые создаются командой:

bs = BookStudy(name, author, year)

где name - название пособия (строка); author - автор пособия (строка); year - год издания (целое число). 
Такие же публичные локальные атрибуты должны быть в объектах класса BookStudy.

Для каждого объекта реализовать вычисление хэша по двум атрибутам: name и author (без учета регистра).

Сформировать список lst_bs из объектов класса BookStudy на основе прочитанных строк (списка lst_in). 
После этого определить число книг с уникальными хэшами. Это число сохранить через переменную unique_books (целое число).

P.S. На экран ничего выводить не нужно.

'''