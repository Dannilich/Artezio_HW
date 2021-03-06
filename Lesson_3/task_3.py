"""
Задание 3:

Написать функцию, которая будет принимать только 4 позиционных аргументы (все аргументы числовые).
Функция должна вернуть среднее арифметическое аргументов и самый большой аргумент за все время вызовов этой функции.

Пример:
foo(1,2,3,4) -> 2.5, 4
foo(-3, -2, 10, 1) -> 1.5, 10

foo(7,8,8,1) -> 6, 10
"""
def avg_and_biggest_for_all_time(a, b, c, d):
    """
    Функция по
    возврату среднеарифметического 4-х чисел
    + вывода наибольшего значения за историю функции

    :param a: 1-ое число
    :param b: 2-ое число
    :param c: 3-е  число
    :param d: 4-ое число
    :return: кортеж (среднеарифмитическое ввода, наибольшее)

    Реализация:
    для хранения наибольшего значения за историю функции
    был добавлен функции аттрибут _biggest,
    если первоначально этого аттрибута нету,
        то он инициализируется максимиальным значением входных параметров
    после условия ему
    присваевается максимальное значение от входных аттрибутов с учётом его,
     т.е.: ( max(args, _biggest) )
    """
    if not hasattr(avg_and_biggest_for_all_time,"_biggest"): avg_and_biggest_for_all_time._biggest =  max(a, b, c, d)
    #строка выше - осознанно большая, скомканная в одну, так как она имеет смысл только при инициализации, поэтому последующие запуски она не не нужна
    avg_and_biggest_for_all_time._biggest = \
        max(avg_and_biggest_for_all_time._biggest, a, b, c, d)
    avg = (a + b + c + d) / 4
    return (avg, avg_and_biggest_for_all_time._biggest)


print(avg_and_biggest_for_all_time(1, 2, 3, 10))
print(avg_and_biggest_for_all_time(5, 2, 7, -4))
print(avg_and_biggest_for_all_time(-1, 8, 3, 8))