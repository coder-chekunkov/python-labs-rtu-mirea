# 3.4: "Числа в строке"

def from_string_to_list(string, container):
    container.append(string)


a = [77, '11 12']
from_string_to_list("", a)
print(*a)
