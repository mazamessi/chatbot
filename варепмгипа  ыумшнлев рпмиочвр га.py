n=input("Введите слово ")
def neger(n, i):
    if n[i]!=n[-1-i]:
        return "Нет"
    elif i<(len(n)+1)//2:
        return neger(n,i+1)
    else:
        return "палиндром"
print(neger("Вася",0))
print(neger("анна",0))
