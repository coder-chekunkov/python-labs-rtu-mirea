# 1.7: "Обратный отсчет"

n = int(input())
if n < 0:
    print("Пуск!")
else:
    for i in range(n, 0, -1):
        print("Осталось секунд:", i)
    print("Пуск!")
