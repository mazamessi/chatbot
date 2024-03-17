pers = {"имя":"Фёдор", "возраст":23,"суперспособность":"умеет переваривать пищу на расстоянии","особенности":"тупой","параметры":"высокий"}
kommand=input("Введите команду ")
while kommand!="Выход":
    if kommand=="параметры":
        print(pers["параметры"])
    elif kommand=="особенности":
        print(pers["особенности"])
    elif kommand=="переделать существующие":
        print(pers)
        name=input("Что вы хотите изменить ")
        print("Старое значение: ",pers[name])
        value=input("Введите новое значение: ")
        pers[name] = value
    elif kommand =="инфа":
        print(pers)
    elif kommand=="добавить значение":
        qwerty=input("Что добавить ")
        ytrewq=input("Введите значение ")
        pers[qwerty]=ytrewq
    kommand=input("Введите команду ")
