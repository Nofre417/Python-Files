# Написать программу которая создает пары из листа при услови что первый элемент пары четный, второй элемент пары возведит в квадрат 

# 1 - Способ
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = list()

for i in data:
    if i % 2 == 0:
        res.append((i, i ** 2))

print(res)

# 2 - Способ

def select(f, col):
    return[f(x) for x in col]

def where(f, col):
    return[x for x in col if f(x)]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = select(int, data)
print(res)

res = where(lambda x: x % 2 == 0 , res)
print(res)

res = list(select(lambda x: (x, x ** 2), res))
print(res)