password=input("Введите пароль")
def pass_check(password):
    if password.isalpha():
        print("Есть буквы")
    if password.isdigit():
        print("Есть буквы")
    if password.islower():
        print("Есть маленькие буквы")
    if password.isupper():
        print("Есть большие буквы")
    if len (password)<8:
        print("Меньше 8 цифр")
    if '!' in password or '=' in password or'@' in password or '#' in password  or'$' in password:
        print("В пароле есть =,@,#,$")
pass_check(password)
        
