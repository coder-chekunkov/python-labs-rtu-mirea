# 2.5: "Напёрстки"

n = int(input())
mas = []

for i in range(n):
    mas.append(input())

ans_mas = []
x = int(input())
for i in range(x):
    buff = int(input())
    ans_mas = []
    for j in range(buff):
        z = int(input())
        ans_mas.append(mas[z - 1])
    mas = ans_mas

for i in ans_mas:
    print(i)


