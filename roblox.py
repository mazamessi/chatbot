import random as r
game=0
mylib=0
pole = [["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","*","*","*","*","*"],
        ["*","*","*","#","*","*","*","#","#","#","#","#"],
        ["*","*","*","#","#","#","#","#","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["#","#","#","#","*","*","*","*","*","#","#","#"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"],
        ["*","*","*","#","*","*","*","*","*","#","*","*"]]
for i in range(3):
    a=r.randint (0,len(pole)-1)
    b=r.randint (0,len(pole)-1)
    pole[a][b]="💣"
vidimost_polya=[["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"]]
def check(stroka,stolb):
    if vidimost_polya[stroka][stolb] == "•":
        vidimost_polya[stroka][stolb] = pole[stroka][stolb]
        if pole[stroka][stolb] == "0":
            if stroka-1 >= 0:
                check(stroka-1,stolb)
                if stolb-1 >= 0:
                    check(stroka-1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka-1,stolb+1)
            if stroka+1 < len(pole):
                check(stroka+1,stolb)
                if stolb-1 >= 0:
                    check(stroka+1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka+1,stolb+1)
            if stolb-1 >= 0:
                    check(stroka,stolb-1)
            if stolb+1 < len(pole[stroka]):
                check(stroka,stolb+1)
def vyvodPolya(spisok):
    for stroka in spisok:
        for kletka in stroka:
            print(kletka,end='')
        print()
def isOpen():
    opened = True
    for stroka in vidimost_polya:
        if "•" in stroka:
            opened = False
    return opened
def digit(pole):
    for stroka in range(len(pole)):
        for stolb in range(len(pole[stroka])):
            bomb=0
            if pole[stroka][stolb]!="💣":
                if stroka-1 >= 0:
                    if pole[stroka-1][stolb]=="💣":
                        bomb=bomb+1
                    if stolb-1 >= 0:
                        if pole[stroka-1][stolb-1]=="💣":
                            bomb=bomb+1
                    if stolb+1 < len(pole[stroka]):
                        if pole[stroka-1][stolb+1]=="💣":
                            bomb=bomb+1
                if stroka+1 < len(pole):
                    if pole[stroka+1][stolb]=="💣":
                            bomb=bomb+1
                    if stolb-1 >= 0:
                        if pole[stroka+1][stolb-1]=="💣":
                            bomb=bomb+1
                    if stolb+1 < len(pole[stroka]):
                        if pole[stroka+1][stolb+1]=="💣":
                            bomb=bomb+1      
                if stolb-1 >= 0:
                    if pole[stroka][stolb-1]=="💣":
                            bomb=bomb+1
                if stolb+1 < len(pole[stroka]):
                    if pole[stroka][stolb-1]=="💣":
                            bomb=bomb+1
                if stolb+1 < len(pole[stroka]):
                    if pole[stroka][stolb+1]=="💣":
                            bomb=bomb+1
                pole[stroka][stolb]=str(bomb)
digit(pole)




































import mylib
game = True
while game:
    n=input("Что вы сделаете этим ходом ")
    if n=="открыть":
        stroka = int(input("Введите номер строки"))
        stolb = int(input("Введите номер столбца"))
        if stroka >12 or stolb >12:
            print("неправильная координата")
        else:
            mylib.check(stroka-1,stolb-1)
            mylib.vyvodPolya(mylib.vidimost_polya)
        if mylib.isOpen():
            game = False
        if mylib.pole[stroka][stolb]=="💣":
            print("Игра окончена")
            break
    else:
        stroka = int(input("Введите номер строки"))
        stolb = int(input("Введите номер столбца"))
        mylib.vidimost_polya[stroka][stolb]="📍"
        if stroka >12 or stolb >12:
            print("неправильная координата")
#         else:
#             mylib.check(stroka-1,stolb-1)
#             mylib.vyvodPolya(mylib.vidimost_polya)
#         if mylib.isOpen():
#             game = False
#         if mylib.pole[stroka][stolb]=="💣":
#             print("Игра окончена")
#             break
print("Всё поле открыто!")
