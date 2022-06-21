class Morph:
    def __init__(self, *args):
        self.lst_words = [s.lower() for s in args]

    def add_word(self, word):
        self.lst_words.append(word.lower())

    def get_words(self):
        return tuple(self.lst_words)

    def __eq__(self, other):
        if not isinstance(other, str):
            raise TypeError("Операнд справа должен иметь тип str")
        return other.lower() in self.lst_words


text = input()

lst_w = [('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
         ('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами', 'формулах'),
         ('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам', 'векторами', 'векторах'),
         ('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам', 'эффектами', 'эффектах'),
         ('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

dict_words = [Morph(*w) for w in lst_w]


lst_text = [t.strip('–?!,.; ') for t in text.split()]

res = sum(w == m for w in lst_text for m in dict_words)
print(res)


# res = 0
# for w in lst_text:
#     for m in dict_words:
#         if w == m:
#             res += 1

'''
Ваша задача написать программу поиска слова в строке. Задача усложняется тем, что слово должно определяться 
в разных его формах. Например, слово:

программирование

может иметь следующие формы:

программирование, программированию, программированием, программировании, программирования, программированиям, 
программированиями, программированиях

Для решения этой задачи необходимо объявить класс Morph (морфология), объекты которого создаются командой:

mw = Morph(word1, word2, ..., wordN)

где word1, word2, ..., wordN - возможные формы слова.

В классе Morph реализовать методы:

add_word(self, word) - добавление нового слова (если его нет в списке слов объекта класса Morph);
get_words(self) - получение кортежа форм слов.

Также с объектами класса Morph должны выполняться следующие операторы сравнения:

mw1 == "word"  # True, если объект mv1 содержит слово "word" (без учета регистра)
mw1 != "word"  # True, если объект mv1 не содержит слово "word" (без учета регистра)

И аналогичная пара сравнений:

"word" == mw1
"word" != mw1

После создания класса Morph, формируется список dict_words из объектов этого класса, для следующих слов с их словоформами:

- связь, связи, связью, связи, связей, связям, связями, связях
- формула, формулы, формуле, формулу, формулой, формул, формулам, формулами, формулах
- вектор, вектора, вектору, вектором, векторе, векторы, векторов, векторам, векторами, векторах
- эффект, эффекта, эффекту, эффектом, эффекте, эффекты, эффектов, эффектам, эффектами, эффектах
- день, дня, дню, днем, дне, дни, дням, днями, днях

Затем, прочитайте строку из входного потока командой:

text = input()

Найдите все вхождения слов из списка dict_words (используя операторы сравнения) в строке text (без учета регистра 
и их словоформы). Выведите на экран полученное число.

Sample Input:

Мы будем эффектом, устанавливать связь! завтра вектора днем.

Sample Output:
2
'''