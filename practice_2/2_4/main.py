# 2.4: "Белый список"

n = int(input())
mas_white_word = []

for i in range(n):
    buff = input()
    mas_white_word.append(buff)

x = int(input())

for i in range(x):
    buff = input()
    if buff in mas_white_word:
        print(buff)
