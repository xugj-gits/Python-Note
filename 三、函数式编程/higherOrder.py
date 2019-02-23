
# -*- coding: UTF-8 -*-

# 定义一个高阶函数 参数f为函数

def add(x, y, f):
    return f(x) + f(y)

result = add(-6, -8, abs)

print(result)