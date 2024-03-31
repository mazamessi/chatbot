users={}
command=input("Что вы хотите сделать ")
while command!="выход":
    if command== "регистрация":
        login= input("Введите логин: ")
        password1=input("Введите пароль: ")
        password2=input("Введите пароль еще раз: ")
        if password1==password2:
            print("Вы зарегистрированы!")
            users[login]=password1
            command=input("Что вы хотите сделать ")
        else:
            print("Что-то не то, повторите еще раз ")
            password2=input("Введите пароль еще раз: ")
    elif command == "авторизация":
        login = input("Введите логин ")
        password = input("Введите пароль ")
        if login in users.keys():
            if password == users[login]:
                print("Успешная авторизация")
            else:
                print("Пароль не верен")
        else:
            print("Такой пользователь не найден")
    command=input("Что вы хотите сделать ")
