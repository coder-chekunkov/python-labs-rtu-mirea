# 3.1: "Скажи «пароль» и проходи"

def ask_password():
    password = "password"
    for i in range(3):
        buff = input()
        if buff == password:
            print("Пароль принят")
            return
    print("В доступе отказано")


ask_password()
