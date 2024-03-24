key={"Фамилия":"Мазутский","Имя":"Иван","Отчество":"Михайлович"}
command={"инглиш":5,"русский":4,"немецкий":5,"труды":5}
kom=input("Введите команду ")
while kom!="Выход":
    if kom=="добавить запись":
        qwerty=input("Что добавить ")
        ytrewq=input("Введите значение ")
        command[qwerty]=ytrewq
    elif kom=="изменить":
        print(command)
        name=input("Что вы хотите изменить ")
        print("Старое значение: ",command[name])
        value=input("Введите новое значение: ")
        command[name]=value
    elif kom=="удалить":
        del command[input()]
        print(command)
        kom=input("Введите команду ")
    else:
        print("Не понял")
    kom=input("Введите команду ")
