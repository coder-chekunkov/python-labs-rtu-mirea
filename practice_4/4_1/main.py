# 4.1: "Генератор визуально различимых паролей (A)"
import random


def main(n, m):
    string = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    passwords = []
    for i in range(n):
        password = ''
        buff = random.sample(range(len(string)), m)
        for j in range(len(buff)):
            password += string[buff[j]]
        passwords.append(password)
    return passwords


def generate_password(m):
    string = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    password = ''
    buff = random.sample(range(len(string)), m)
    for i in range(len(buff)):
        password += string[buff[i]]
    return password


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
