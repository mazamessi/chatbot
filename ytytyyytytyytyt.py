qwertyuiopasdfghjklzxcvbnm={"мой лучший день":"это","игры":"call of duty","рацион":"поесть,поспать,поиграть","уроки":"прогуляю"}
print(qwertyuiopasdfghjklzxcvbnm)
command=input("Вы что-то хотите добавить ")
while command!="нет":
    if command =="да":
        qwerty=input("Что добавить ")
        ytrewq=input("Введите значение ")
        qwertyuiopasdfghjklzxcvbnm[qwerty]=ytrewq
        print(qwertyuiopasdfghjklzxcvbnm)
    else:
        print("Не понял")
        break
    command=input("Вы что-то хотите добавить ")
