"""
Задание 1:

Написать несколько функций,
которые в качестве единственного аргумента принимают список (или кортеж) целых чисел.
  1 функция должна вернуть квадраты элементов коллекции; (squares)
  2 функция должна вернуть только элементы на четных позициях; (even_positions_values)
  3 функция возвращает кубы четных элементов на нечетных позициях.(qubes_of_uneven_positions)
"""
def squares(nums):
    """
    №1 Функция квадратов:

    Аргументы: список или кортеж
    Возврат: словарь вида: {число : его квадрат}(словарь для ясности)
    """
    squares_dict = dict()
    for num in nums:
        squares_dict.update({num: num * num})
    return squares_dict


print(squares(range(1, 10 + 1)))


def even_positions_values(values):
    """
    №2 Функция по возврату элементов на чётных позициях:

    Аргументы: список или кортеж значений
    Возврат: список элементов стоящих на чётных позициях
    Реалицаия: через чётное чередование вносить в итоговый список
    """
    list_of_values = list()
    next_is_even = False
    for val in values:
        if next_is_even:
            list_of_values.append(val)
            next_is_even = False
        else:
            next_is_even = True
    return list_of_values


print(even_positions_values(range(1, 10 + 1)))


def qubes_of_uneven_positions(args):
    """
    №3 Функция по возврату кубов от чисел на нечётной позиции

    Аргументы: список или кортеж чисел
    Возврат: словарь вида: {число : число^3}
    Реализация: через нечётное чередование добавлять элемент словаря кубов
    """
    qubes = dict()
    next_is_uneven = True
    for num in args:
        if next_is_uneven:
            qubes.update({num: num ** 3})
            next_is_uneven = False
        else:
            next_is_uneven = True
    return qubes


print(qubes_of_uneven_positions(range(1, 10 + 1)))
