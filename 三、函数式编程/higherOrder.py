
# -*- coding: UTF-8 -*-

from functools import reduce

# 定义一个高阶函数 参数f为函数

def add(x, y, f):
    return f(x) + f(y)

result = add(-6, -8, abs)

print(result)

# map()函数 演示

def square(x):
    return x * x

a = map(square, [1, 2, 3])

print(a)

print(list(a))

# reduce() 函数演示

def f1(x, y):
    return x + y

b = reduce(f1, [1, 2, 3])

print(b)

# filter() 函数演示
# 过滤列表中所有奇数

def is_odd(x):
    return x % 2 == 1


filterObj = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(filterObj)

print(list(filterObj))