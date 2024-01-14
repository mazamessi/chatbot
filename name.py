import random as r
def random_digit():
    e=r.randint(100,999)
    return e

def check(a,b):
    if a==b:
        print("Молодец правильно!")
    else:
        print("неправильно")
   
def check(a,b):
    if a==b:
        print("Молодец правильно!")
    elif str(a)[0] == str(b)[0] or str(a)[1] == str(b)[1]or str(a)[2] == str(b)[2]:
        print("Горячо")
    elif str(b)[0] in str(a) or str(b)[1] in str(a) or str(b)[2] in str(a):
        print("Тепло")
    else:
        print("холодно")
rf=random_digit()
k=int(input("Введите число "))
while 1:
    check(k,rf)
    k=int(input("Введите число "))
