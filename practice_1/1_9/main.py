# 1.9: "Таблица деления"

a = int(input())
b = int(input())

for i in range(1, b + 1):
    buff_str = ""
    for j in range(1, a + 1):
        buff = float(j / i)
        buff_str = buff_str + str(buff) + " "
    print(buff_str)
