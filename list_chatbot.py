empty=["Поесть","поспать","поиграть"]
comand=input("Введите команду ")
while comand !='выход':
    if comand=="добавить":
        empty.append(input("Что добавить "))
    elif comand=="удалить":
        empty.remove(input("Что удалить "))
    elif comand=="показать по индексу":
        print(empty[int(input("Впишите индекс "))])
    elif comand=="показать весь список":
        print(empty)
    comand=input("Введите команду ")
