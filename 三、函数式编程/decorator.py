# -*- coding: UTF-8 -*-
from datetime import datetime

# 装饰器 示例

# 定义一个装饰器

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 定义一个函数

@log
def now():
    print(datetime.now())


if __name__ == '__main__':
    now()