# 2.3: "Розенкранц и Гильденстерн меняют профессию"

string = input()
maximum = -1
buff = 0

for i in range(len(string) - 1):
    if string[i] == "о" and string[i + 1] == "о":
        buff += 1
        if buff >= maximum:
            maximum = buff
    else:
        buff = 1



print(maximum)
