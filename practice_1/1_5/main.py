# 1.5: "Среднее"

kol = 0
count = 0

while True:
    buff = float(input())
    if buff < -300:
        break
    else:
        kol += 1
        count += buff

print(count / kol)
