import inspect
from pprint import pprint


def introspection_info(obj):
    # тип объекта
    type_ = type(obj)

    # возвращает отсортированный список атрибутов и методов, доступных
    # для указанного объекта, который может быть переменной или функцией
    first_list = []
    second_list = []
    count = 0
    for i in dir(obj):
        count += 1
        if i.startswith('__'):
            first_list.append(i)
        else:
            second_list.append(i)

    # возвращает из какого модуля мы взяли объект
    module_ = inspect.getmodule(obj)

    # id объекта
    id_ = id(obj)

    # название функции
    name_ = obj.__name__

    # можем ли мы вызвать этот объект
    calab_ = callable(obj)

    # является ли функцией
    func_ = inspect.isfunction(obj)

    return {'Тип': type_,
            "Атрибуты": first_list,
            "Методы": second_list,
            "obj из модуля": module_,
            "id": id_,
            "Название": name_,
            "Можем ли мы вызвать функцию": calab_,
            'Является фнкцией': func_}


introspect = introspection_info(str)
pprint(introspect)