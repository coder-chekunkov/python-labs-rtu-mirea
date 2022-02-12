# 1.2: "Регистрация почты"

login = input()
mail = input()

if '@' in login:
    bool_login = False
else:
    bool_login = True

if '@' in mail:
    bool_mail = True
else:
    bool_mail = False

if bool_mail and bool_login:
    print("OK")
else:
    if not bool_mail:
        print("Некорректный адрес")
    if not bool_login:
        print("Некорректный логин")
