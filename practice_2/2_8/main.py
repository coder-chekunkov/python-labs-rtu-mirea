# 2.8: "CSV 2.0"

n = int(input())
mas = []
for i in range(n):
    buff_string = input()

    buff_mas = buff_string.split(",")
    mas.append(buff_mas)

x = int(input())
for i in range(x):
    buff = input()
    a, b = buff.split(",")
    a = int(a)
    b = int(b)
    print(mas[a][b])
