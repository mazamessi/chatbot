a=int(input("Введите меньшее число "))
b=int(input("Введите большее число "))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for g in range(a,b-1,-1):
        print(g)















a=int(input("Введите меньшее число "))
b=int(input("Введите большее число "))
def nigers(a,b):
    if a<b:
        for i in range(a,b+1):
            print(i)
    else:
        for g in range(a,b-1,-1):
            print(g)
nigers(a,b)
