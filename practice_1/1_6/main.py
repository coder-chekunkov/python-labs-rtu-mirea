# 1.6: "Остров невезения"

d = int(input())
m = int(input())
y = int(input())

if m - 2 > 0:
    y = y
    m -= 2
else:
    y -= 1
    m = 12 - abs(m - 2)

c = y // 100

y = y % 100
ans = int(d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777))
buff = ans % 7
if buff == 0:
    print(7)
else:
    print(buff)
