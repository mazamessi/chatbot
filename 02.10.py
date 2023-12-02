z=int(input("Введите пароль "))
def pass_check(z):
    if 10<z and 99>z:
        print("2-х значное ")
    elif 100<z and 999>z:
        print("3-х значное ")
    else:
        print("пароль неверный ")
pass_check(z)
