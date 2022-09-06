# This modul is generated by main.py
"""Модуль удобства парсирования сведений"""


exception_regular = {
            'Экз. № _____': '',
            'Экз.№_____ из __3__': '',
            'Экз.№__1__ из __3__': '',
            'Экз.№_____ из __5__': '',
            'на упаковку (партию) радиоактивных отходов №': 'Номер паспорта',
            'на упаковку радиоактивных отходов № Наимен': 'Номер паспорта',
            'на упаковку радиоактивных отходов №': 'Номер паспорта',
            'Номер контракта передачи РАО на захоронение': 'Номер договора передачи РАО на захоронение',
            }

def remove_values_from_list(the_list, val):
    """ Функция для очистки пробелов в строке между значениями """
    # i список в списке списков
    for i in the_list:
        while val in i:
            i.remove(val)
    
    return the_list

# def remove_values_from_list(the_list, val):
#     """ Функция для очистки пробелов в строке между значениями """
#     while val in the_list:
#         the_list.remove(val)
#     return the_list


def replace_values(exception: dict, exception_list: list):
    """ Замена значений на необходимые сведения для шаблонирования"""
    for x,y in zip(exception.keys(), exception.values()):
        exception_list_end = [str(i).replace(x, y) for i in exception_list]

    return exception_list_end




# horrisontally
# remove_values_from_list(flat_list, "")
# # используем функцию из модуля exception.py
# flat_list = replace_values(exception_regular, flat_list)

# vertically
# flat_list = [str(i).replace('\r\n', ' ') for i in flat_list]