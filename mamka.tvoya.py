n = int(input('Для какого числа посчитать факториал?'))
def fact(num):
    if num > 1:
        return 1
    else:
        print(num, end=' ')
        return fact(num-1)
fact(n)
