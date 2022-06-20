class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, matrix, *args, **kwargs):
        self.check_matrix(matrix)
        return self.step_2(self.step_1(matrix))

    def step_1(self, m):
        matrix1 = []
        for k in range(len(m)):
            line1 = []
            for i in range(0, len(m[0]), self.step[0]):
                if i + self.size[0] <= len(m[0]):
                    line1.append(max([m[k][j] for j in range(i, i + self.size[0])]))
            matrix1.append(line1)
        return matrix1

    def step_2(self, m):
        matrix1 = []

        for k in range(len(m[0])):
            row = []
            for i in range(0, len(m), self.step[1]):
                if i + self.size[1] <= len(m):
                    row.append(max([m[j][k] for j in range(i, i + self.size[1])]))
            matrix1.append(row)
        line = []
        res_m = []
        for i in range(len(matrix1[0])):
            line.append([matrix1[j][i] for j in range(len(matrix1))])
        res_m.extend(line)
        return res_m

    def check_matrix(self, matrix):
        if self.get_depth(matrix) != 2:
            raise ValueError("Неверный формат для первого параметра matrix.")
        len_x = len(matrix)
        len_y = len(matrix[0])
        for i in range(len_x):
            if len(matrix[i]) != len_y:
                raise ValueError("Неверный формат для первого параметра matrix.")
            for j in range(len_y):
                if type(matrix[i][j]) not in (int, float):
                    raise ValueError("Неверный формат для первого параметра matrix.")

    def get_depth(self, l):
        if isinstance(l, (list, tuple)):
            t = []
            for itm in l:
                t += self.get_depth(itm),
            return 1 + (max(t) if t else 0)
        return 0


mp = MaxPooling(step=(2, 2), size=(2,2))
res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2], [5, 4, 3, 2], [5, 4, 3, 2]])    # [[6, 8], [9, 7]]
print(res)

'''
Объявите класс Dimensions (габариты) с атрибутами:

MIN_DIMENSION = 10
MAX_DIMENSION = 10000

Каждый объект класса Dimensions должен создаваться командой:

d3 = Dimensions(a, b, c)   # a, b, c - габаритные размеры

Значения a, b, c должны сохраняться в локальных приватных атрибутах __a, __b, __c объектах этого класса.

Для изменения и доступа к приватным атрибутам в классе Dimensions должны быть объявлены объекты-свойства (property) 
с именами: a, b, c. Причем, в момент присваивания нового значения должна выполняться проверка попадания числа в диапазон 
[MIN_DIMENSION; MAX_DIMENSION]. Если число не попадает, то оно игнорируется и существующее значение не меняется.

С объектами класса Dimensions должны выполняться следующие операторы сравнения:

dim1 >= dim2   # True, если объем dim1 больше или равен объему dim2
dim1 > dim2    # True, если объем dim1 больше объема dim2
dim1 <= dim2   # True, если объем dim1 меньше или равен объему dim2
dim1 < dim2    # True, если объем dim1 меньше объема dim2

Объявите в программе еще один класс с именем ShopItem (товар), объекты которого создаются командой:

item = ShopItem(name, price, dim)

где name - название товара (строка); price - цена товара (целое или вещественное число); dim - габариты товара (объект класса Dimensions).

В каждом объекте класса ShopItem должны создаваться локальные атрибуты:

name - название товара;
price - цена товара;
dim - габариты товара (объект класса Dimensions).

Создайте список с именем lst_shop из четырех товаров со следующими данными:

- кеды; 1024; (40, 30, 120)
- зонт; 500.24; (10, 20, 50)
- холодильник; 40000; (2000, 600, 500)
- табуретка; 2000.99; (500, 200, 200)

Сформируйте новый список lst_shop_sorted с упорядоченными по возрастанию объема (габаритов) товаров списка lst_shop, 
используя стандартную функцию sorted() языка Python и ее параметр key для настройки сортировки. Прежний список lst_shop должен оставаться без изменений.

P.S. На экран в программе ничего выводить не нужно.
'''