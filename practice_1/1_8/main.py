# 1.8: "Найди кота"

n = int(input())
isCat = False

for i in range(n):
    buff = input()
    if "Кот" in buff or "кот" in buff:
        isCat = True

if isCat:
    print("МЯУ")
else:
    print("НЕТ")
