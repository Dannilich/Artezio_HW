#получение строки full name
import sys 
"""
Если колчичество входных параметров больше 1
(если в них не только путь к файлу)
то мы берем параметры входа как full name,
Иначе вручную считываем
""" 
if len(sys.argv) > 1:
    #print(sys.argv)
    full_name = sys.argv[1:]
else:
    full_name = input("input your full name: ")
    full_name = full_name.strip().split(' ')


"""
Далее разбиваем строку на подстроки,
где потом построично преобразуем к нужному формату
"""
for num in range(len(full_name)) :
    full_name[num] = full_name[num].capitalize()
    #print(full_name[num])


"""
Далее конкатенируем в единую строку
и выводим
"""
full_name = " ".join(full_name)
print("correct full name is: "+full_name)

"""
ставим на паузу 
для ознакомленя с результатом
"""
import os
os.system("pause")