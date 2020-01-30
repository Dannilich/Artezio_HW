def count_of_dividing_in_range(begin,end, deviding_num):
    count = 0
    for num in range(begin,end+1):
        count += num % deviding_num == 0
        #print(num,num % deviding_num == 0)
    return count

print(count_of_dividing_in_range(0,10,2)) #странно, что ноль делиться на 2
    