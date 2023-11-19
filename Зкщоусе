from random import randint
v=0
n=int(input("Сколько символов загадать "))
metok=list(['false']*n)
print(n)
if n == 1:
    v=randint(0,9)
elif n == 2:
    v=randint(10,99)
elif n == 3:
    v=randint(100,999)
elif n == 4:
    v =randint(1000,9999)
while 1:
    b=int(input("Отгадай "))
    for i in range(n):
        if str(v)[i]==str(b)[i]:
            metok[i]='right'
        else:
            metok[i]='false'
    print(metok)
    if v==b:
        print("You win")
        break
