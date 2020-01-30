n = int(input("Введите конец диапозона квадратов от нечётных чисел: "))

def squares_of_odd(n_range):
    count = 0
    for num in range(0,n_range):
        if num %2 != 0:
            print("Число: ",num,"  Квадрат:",num**2)
            count +=1
    print("Количество: ",count)

squares_of_odd(n)