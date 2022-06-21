stich = ["Я к вам пишу – чего же боле?",
        "Что я могу еще сказать?",
        "Теперь, я знаю, в вашей воле",
        "Меня презреньем наказать.",
        "Но вы, к моей несчастной доле",
        "Хоть каплю жалости храня,",
        "Вы не оставите меня."]


class StringText:
    def __init__(self, lst_words):
        self.lst_words = lst_words

    def __lt__(self, other):
        if not isinstance(other, StringText):
            raise TypeError("Операнд справа должен иметь тип StringText")
        return len(self.lst_words) < len(other.lst_words)

    def __le__(self, other):
        if not isinstance(other, StringText):
            raise TypeError("Операнд справа должен иметь тип StringText")
        return len(self.lst_words) <= len(other.lst_words)

    def len_st(self):
        return len(self.lst_words)


lst_text = []
for s in stich:
    st = s.replace('–', '')
    lst = st.split()
    lst_words = list(map(lambda x: x.strip('–?!,.;'), lst))
    lst_text.append(StringText(lst_words))

lst_text_sorted = sorted(lst_text, key=StringText.len_st, reverse=True)
lst_text_string = []
for text in lst_text_sorted:
    lst_str = ' '.join(i for i in text.lst_words)
    lst_text_string.append(lst_str)
lst_text_sorted = lst_text_string

print(lst_text_sorted)


'''
Имеется стихотворение, представленное следующим списком строк:

Необходимо в каждой строчке этого стиха убрать символы "–?!,.;" и разбить ее по словам (слова разделяются одним 
или несколькими пробелами). На основе полученного списка слов, создать объект класса StringText командой:

st = StringText(lst_words)

где lst_words - список из слов одной строчки стихотворения. 

С объектами класса StringText должны быть реализованы операторы сравнения:

st1 > st2   # True, если число слов в st1 больше, чем в st2
st1 >= st2  # True, если число слов в st1 больше или равно st2
st1 < st2   # True, если число слов в st1 меньше, чем в st2
st1 <= st2  # True, если число слов в st1 меньше или равно st2

Все объекты класса StringText (для каждой строчки стихотворения) сохранить в списке lst_text. Затем, сформировать 
новый список lst_text_sorted из отсортированных объектов класса StringText по убыванию числа слов. Для сортировки 
использовать стандартную функцию sorted() языка Python. 
После этого преобразовать данный список (lst_text_sorted) в список из строк (объекты заменяются на соответствующие 
строки, между словами ставится пробел).
'''