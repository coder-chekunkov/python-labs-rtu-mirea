# 3.3: "Счастливый пассажир"

def lucky(a):
    buff_a = str(a)
    len_a = len(buff_a)
    if len_a != 6:
        buff_a = "0" * (6 - len_a) + buff_a

    isFirst = False
    isSecond = False

    lst = list(map(int, list(buff_a)))
    first, last = lst[:3], lst[3:]
    if sum(first) == sum(last):
        isFirst = True

    lst1 = list(map(int, list(str(lastTicket))))
    first1, last1 = lst1[:3], lst1[3:]
    if sum(first1) == sum(last1):
        isSecond = True

    if isFirst and isSecond:
        return "Счастливый"
    else:
        return "Несчастливый"


lastTicket = 123321
print(lucky(110011))
