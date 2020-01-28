import sys 
"""
Если колчичество входных параметров больше 1
(если в них не только путь к файлу)
то мы берем параметры входа как входную строку,
Иначе вручную считываем
""" 
if len(sys.argv) > 1:
    #print(sys.argv)
    string = "".join(sys.argv[1:])
else:
    string = input("input string: ")

"""
Импортируем коллекцию словаря-счётчика,
который из конструктора считает все символы строки
и выводим все символы с их количеством
"""
import collections
chars_dict = collections.Counter(string)
print("Counter of symbols:")
print(chars_dict)

"""
ставим на паузу 
для ознакомленя с результатом
"""
import os
os.system("pause")
