# 2.1: "Книги на лето"

n = int(input())
x = int(input())
mas = []

for i in range(n):
    buff = input()
    mas.append(buff)

for i in range(x):
    buff = input()
    if buff in mas:
        print("YES")
    else:
        print("NO")
