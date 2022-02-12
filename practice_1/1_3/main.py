# 1.3: "Калькулятор"

a = float(input())
b = float(input())
sign = input()

if sign == "+":
    print(a + b)
elif sign == "-":
    print(a - b)
elif sign == "*":
    print(a * b)
elif sign == "/":
    if b == 0:
        print("888888")
    else:
        print(a / b)
else:
    print("888888")
