# 2.7: "Гэтсби"

symbol = input()
string = input()
mas = string.split(' ')

for i in mas:
    if symbol in i or symbol.capitalize() in i:
        print(i)
