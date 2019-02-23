# -*- coding: UTF-8 -*-

def fib(max):
    print('普通实现：')
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'

# fib(6)

"""
利用生成器（generator） 实现 斐波拉契数列
"""
def gfib(max):
    print('generator实现：')
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in gfib(6):
    print(n)
