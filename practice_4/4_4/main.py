# 4.4: "Генератор визуально различимых паролей (A + B)"
import random


def main(n, m):
    passwords = []
    for i in range(n):
        passwords.append(generate_password(m))
    return passwords


def generate_password(m):
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    string_lower = "abcdefghijkmnpqrstuvwxyz"
    string_upper = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    string_numbers = "23456789"
    password = ''
    buff = []
    a = random.randint(0, len(string_lower) - 1)
    buff.append(string_lower[a])
    b = random.randint(0, len(string_upper) - 1)
    buff.append(string_upper[b])
    c = random.randint(0, len(string_numbers) - 1)
    buff.append(string_numbers[c])
    for i in range(m - 3):
        while True:
            d = random.randint(0, len(alphabet) - 1)
            if not alphabet[d] in buff:
                buff.append(alphabet[d])
                break
    for i in range(len(buff)):
        password += buff[i]
    return password


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
