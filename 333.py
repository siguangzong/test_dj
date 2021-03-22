from functools import reduce


def func(x, y):
    return x + y;

c = reduce(func, [1, 2, 3])
print(c)
