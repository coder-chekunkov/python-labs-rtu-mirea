# 4.3: "Найти приближённое значение Пи"
import random

k = 0.0
for i in range(500000):
    x = random.random()
    y = random.random()
    k += (x * x + y * y < 1.0)
print(4 * k / 500000)
