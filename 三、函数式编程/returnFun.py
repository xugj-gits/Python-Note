# -*- coding: UTF-8 -*-

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

fun = lazy_sum(1, 2, 3)

print(fun)
print(fun())

# 闭包举例

def count():
    def f(j):
        return lambda : j * j
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1)
print(f1())

print(f2)
print(f2())

print(f3)
print(f3())