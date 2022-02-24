# 4.2: "Генератор визуально различимых паролей (B)"
import random


def generate_password(m):
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    string_lower = "abcdefghijkmnpqrstuvwxyz"
    string_upper = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    string_numbers = "23456789"
    password = ''
    a = random.randint(0, len(string_lower) - 1)
    password += string_lower[a]
    b = random.randint(0, len(string_upper) - 1)
    password += string_upper[b]
    c = random.randint(0, len(string_numbers) - 1)
    password += string_numbers[c]

    buff = random.sample(range(len(alphabet)), m - 3)
    for i in range(len(buff)):
        password += alphabet[buff[i]]
    return password


def main(n, m):
    alphabet = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
    string_lower = "abcdefghijkmnpqrstuvwxyz"
    string_upper = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    string_numbers = "23456789"
    passwords = []
    for i in range(n):
        password = ''
        a = random.randint(0, len(string_lower) - 1)
        password += string_lower[a]
        b = random.randint(0, len(string_upper) - 1)
        password += string_upper[b]
        c = random.randint(0, len(string_numbers) - 1)
        password += string_numbers[c]

        buff = random.sample(range(len(alphabet)), m - 3)
        for j in range(len(buff)):
            password += alphabet[buff[j]]
        passwords.append(password)
    return passwords


print("Случайный пароль из 7 символов:", generate_password(7))
print("10 случайных паролей длиной 15 символов:")
print(*main(10, 15), sep="\n")
