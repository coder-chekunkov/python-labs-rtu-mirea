# 1.4: "Сколько строк?"

word = input()
kol = 0

while True:
    if word == "Спасибо.":
        kol += 1
        break
    else:
        kol += 1
        word = input()

print(kol)
