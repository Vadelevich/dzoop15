def calc_salt(weight):
    return int(weight) / 10


# вызовы фукнции
try:
    print(calc_salt(2000))
    print(calc_salt('2000'))
    print(calc_salt('abc'))
except ValueError as v:
    print(v)
    print(0.0)

# результаты вывода
# 20.0
# 20.0
# invalid literal for int() with base 10: 'abc'
# 0.0
