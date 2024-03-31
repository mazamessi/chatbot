from operator import itemgetter
records={}
command=input("Что вы хотите сделать ")
while command!="выход":
    if command =="внести":
        name=input()
        value=input()
        records[name]=value
    elif command =="изменить":
        prin=input("У кого вы хотите изменить ")
        print("Старое значение: ",records[prin])
        value=input("Введите новое значение: ")
        if records[prin]>=value:
            print("Старое значение больше нового")
        else:
            records[prin]=value
    elif command=="вывести":
        s=dict(sorted(records.items(),key=itemgetter(1),reverse=True))
        print(s)
    else:
        print("не понял, повторите")
    command=input("Что вы хотите сделать ")
