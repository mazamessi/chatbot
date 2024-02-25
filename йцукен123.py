








pole = [['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', '*', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O']]
x = 3
y = 4
for stroka in pole:
    for kvadr in stroka:
        print(kvadr, end = ' ')
    print()
command = input("Введи команду: ")
while command != "стоп":
    if command == "пр":
        if x<6:
            pole[y][x] = "O"
            x = x + 1
            pole[y][x] = "*"
    elif command == "лв":
        if  x >0:
            pole[y][x] = "O"
            x = x - 1
            pole[y][x] = "*"
    elif command == "вх":
        if y >0:
            pole[y][x] = "O"
            y = y - 1
            pole[y][x] = "*"
    elif command == "нз":
        if y < 7:
            pole[y][x] = "O"
            y = y + 1
            pole[y][x] = "*"
    else:
        print("Не понял...")
    for stroka in pole:
        for kvadr in stroka:
            print(kvadr, end = ' ')
        print()
    command = input("Введи команду: ")

