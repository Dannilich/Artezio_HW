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
    source_string = input("input the string: ")

"""
Если количество символов 
позволяет нам взять по 2 с каждой стороны,
то берем их, иначе возвращаем "пустую строку"
"""
if(len(source_string) > 1):
    first_2_chars = source_string[:2]
    last_2_chars  = source_string[-2:]
    result_string = first_2_chars + last_2_chars
else:
    result_string = "Empty string"# или " "

print("Result is: "+result_string)
"""
ставим на паузу 
для ознакомленя с результатом
"""
import os
os.system("pause")