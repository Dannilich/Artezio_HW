import functools
def factorial(n):
    if n == 0: return 1
    result = 1
    #return functools.reduce(lambda x,y: x*y, list(range(1,n+1))) #функциональный подход
    for num in range(1,n+1):
        result *= num
    return result

print(factorial(3))