import inspect
import sys
from pprint import pprint

class Introspection:
    def __init__(self):
        self.name = 'Danil'

    def introspection_info(obj):
        pass

# название функции
print(Introspection.introspection_info.__name__)

# тип объекта или объекта
print(type(Introspection.introspection_info))

# тип экземпляра метода (или атрибута)
print(type(Introspection.introspection_info.__get__))

# возвращает отсортированный список атрибутов и методов, доступных
# для указанного объекта, который может быть переменной или функцией
pprint(dir(Introspection.introspection_info))

# проверка на существование атрибута
intros = Introspection()
print(hasattr(intros, 'name'))

# получение атрибута
print(getattr(intros, 'name'))
print(getattr(intros, 'Danil', 'нету'))

# можем ли мы вызвать этот объект
print(callable(intros.introspection_info))

# является ли объект экземпляром указанного класса
print(isinstance(intros, Introspection), '\n')

# inspect - собирает удобные методы и классы для отображения интроспективной информации
# является ли библиотекой
print(inspect.ismodule(sys))
print(inspect.ismodule(intros))
# является ли классом
print(inspect.isclass(sys))
print(inspect.isclass(Introspection))
# является ли функцией
print(inspect.isfunction(sys))
print(inspect.isfunction(Introspection.introspection_info))
# встроенная ли в Python
print(inspect.isbuiltin(sys))
print(inspect.isbuiltin(round))
# возвращает из какого модуля мы взяли объект
type_ = inspect.getmodule(intros)
print(type(type_), inspect.getmodule(Introspection), '\n')

# sys - позволяет работать с настройками интерпретатора
# путь к интерпретатору Python
print(sys.executable)

# операционная система
print(sys.platform)

# текущая версия Python
print(sys.version)
print(sys.version_info, '\n')

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# позволяет расширить глубину нашего стека
sys.setrecursionlimit(5000)
# позволяет увеличить длину строки
sys.set_int_max_str_digits(10000)
print(factorial(2000))
# размер объекта в байтах
print(sys.getsizeof(Introspection))