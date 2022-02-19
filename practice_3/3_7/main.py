# 3.7: "Есть ли 0"

mas = []

for i in range(10):
    mas.append(input())

print(any(['0' in i.split() for i in mas]))
