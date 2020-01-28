import sys
"""
Если колчичество входных параметров больше 1
(если в них не только путь к файлу)
то мы берем параметры входа как входную строку,
Иначе вручную считываем
"""
if(len(sys.argv) > 1):
    source_string = " ".join(sys.argv[1:])
else:
    source_string = input("input string: ")

list_of_strings = source_string.split(' ')

def is_ok(string):
    if(len(string)):
        first_leter = string[0]
        last_leter = string[-1:]
        return (first_leter == last_leter)
    else:
        return False

count_of_correct_strings = len( list(filter(is_ok, list_of_strings))  )
print(count_of_correct_strings)

"""
ставим на паузу 
для ознакомленя с результатом
"""
import os
os.system("pause")