class Handler:
    def __init__(self, methods=('GET',)):
        self.__methods = methods

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'

    def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            if not request['method'] or request['method'] == 'GET' and 'GET' in self.__methods:
                return self.get(func, request)
            elif request['method'] in self.__methods:
                return self.post(func, request)
        return wrapper


@Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "POST", "url": "contact.html"})
print(res)



'''
Пример
 def __call__(self, func):
        def wrapper(request, *args, **kwargs):
            self.__method = request.get('method','GET')
            if self.__method not in self.__allowed_methods:
                return None
            return getattr(self, str(self.__method).lower())(func, request, args, kwargs)
        return wrapper

Необходимо объявить класс-декоратор с именем Handler, который можно было бы применять к функциям, следующим образом:

Здесь аргумент methods декоратора Handler содержит список разрешенных запросов для обработки. Сама декорированная 
функция вызывается по аналогии с предыдущим подвигом:



В результате функция contact должна возвращать строку в формате:

"<метод>: <данные из функции>"

В нашем примере - это будет:

"POST: Сергей Балакирев"

Если ключ method в словаре request отсутствует, то по умолчанию подразумевается GET-запрос. Если ключ method принимает 
значение отсутствующее в списке methods декоратора Handler, например, "PUT", то декорированная функция contact 
должна возвращать значение None.

Для имитации GET и POST-запросов в классе Handler необходимо объявить два вспомогательных метода с сигнатурами:

def get(self, func, request, *args, **kwargs) - для имитации обработки GET-запроса
def post(self, func, request, *args, **kwargs) - для имитации обработки POST-запроса

В зависимости от типа запроса должен вызываться соответствующий метод (его выбор в классе можно реализовать методом 
__getattribute__()). На выходе эти методы должны формировать строки в заданном формате.

'''