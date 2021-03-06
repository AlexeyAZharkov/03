class FileAcceptor:
    def __init__(self, *args):
        self.lst_ext = [s.lower() for s in args]

    def __add__(self, other):
        return FileAcceptor(*set(self.lst_ext + other.lst_ext))

    def __call__(self, filename, **kwargs):
        return filename.split('.')[-1] in self.lst_ext

    def __str__(self):
        return ' '.join(self.lst_ext)


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
print(acceptor12)

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
# acceptor_docs = FileAcceptor("txt", "doc", "xls")
acceptor_docs = FileAcceptor("txt")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)
# filenames = list(filter(acceptor, filenames))

'''
Перед вами стоит задача выделения файлов с определенными расширениями из списка файлов, например:

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

Для этого необходимо объявить класс FileAcceptor, объекты которого создаются командой:

acceptor = FileAcceptor(ext1, ..., extN)

где ext1, ..., extN - строки с допустимыми расширениями файлов, например: 'jpg', 'bmp', 'jpeg'.

После этого предполагается использовать объект acceptor в стандартной функции filter языка Python следующим образом:

filenames = list(filter(acceptor, filenames))

То есть, объект acceptor должен вызываться как функция:

acceptor(filename) 

и возвращать True, если файл с именем filename содержит расширения, указанные при создании acceptor, и False - 
в противном случае. Кроме того, с объектами класса FileAcceptor должен выполняться оператор:

acceptor12 = acceptor1 + acceptor2

Здесь формируется новый объект acceptor12 с уникальными расширениями первого и второго объектов. Например:

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")

Пример использования класса (эти строчки в программе писать не нужно):

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames))

P.S. На экран в программе ничего выводить не нужно.
'''