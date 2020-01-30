
#не знаю как сделать тут ad-hoc полиморфизм
#кроме как сделать аналогичную функцию с другим именем 
# и ссылаться на базовую

# def oldovii_range(end):
#     return oldovii_range(0, end, 1)

def oldovii_range(start, end, step = 1):
    if step == 0: return None
    num = start
    while(True):
        if num > end:
            break
        else:
            yield num
            num += step

#проверка
# for num in oldovii_range(0,10,2):
#     print(num)
    