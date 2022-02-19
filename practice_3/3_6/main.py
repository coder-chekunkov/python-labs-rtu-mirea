# 3.6: "Мимикрия"

transformation = lambda x: x

values = [1, 23, 42, "abc"]
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
