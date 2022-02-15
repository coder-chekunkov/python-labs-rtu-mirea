# 2.2: "Какая-то там книга"

string = input()
n = int(input())

if n < 1 or n > len(string):
    print("Ошибка")
else:
    print(string[n - 1])
