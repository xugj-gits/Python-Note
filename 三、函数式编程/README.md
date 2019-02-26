# 函数式编程

![avatar](函数式编程.png)

### 1. 高阶函数

把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。

- 变量可以指向函数(其他部分语言变量=函数的返回值)
    ```
    >>> a = abs
    >>> a
    <built-in function abs>
    >>> a(-10)
    10
    ```
    > \<built-in function abs> 内置函数 abs
- 函数名也是变量：函数名其实就是指向函数的变量！
    ```
    >>> abs
    <built-in function abs>
    ```
- 函数的参数可以也是函数
    函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
    
###### 1.1 map() 函数
map()是 Python 内置的高阶函数，它接收一个函数 f 和一个可迭代对象，并通过把函数 f 依次作用在可迭代对象的每个元素上，map对象。

    ```
    >>> def square(x):
    ...     return x * x
    ... 
    >>> a = map(square, [1, 2, 3])
    >>> print(a)
    <map object at 0x10f29ae80>
    >>> print(list(a))
    [1, 4, 9]
    ```
###### 1.2 reduce() 函数

reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
<font color = 'red'>reduce函数在python3的内建函数移除了，放入了functools模块</font>

> functools.reduce(function, iterable[, initializer])


```
>>> from functools import reduce
>>> def f(x, y):
...     return x + y
... 
>>> reduce(f, [1, 2, 3])
6
>>> reduce(lambda x, y: x +y ,[1, 2, 3])
6
```

###### 1.3 filter() 函数

> filter(function, iterable)

- filter()函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
- 接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判断，返回True或False，将返回True的元素放到新列表中。
- filter()函数返回值是filter对象
```
>>> #过滤列表中所有奇数
>>> def is_odd(n):
...     return n % 2 == 1
... 
>>> newlist = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
>>> print(newlist)
[1, 3, 5, 7, 9]
```
###### 1.4 sorted() 函数

> sorted（iterable，*，key = None，reverse = False ）

返回一个新的排序后的list

```
>>> sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
>>> sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
[1, 2, 3, 4, 5]
```

```
>>> sorted("This is a test string from Andrew".split(), key=str.lower)
['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
```
> key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。

### 2. 返回函数

###### 2.1 函数作为返回值

高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

```
>>> def lazy_sum(*args):
...     def sum():
...             ax = 0;
...             for n in args:
...                     ax = ax + n
...             return ax
...     return sum
... 
>>> f = lazy_sum(1, 2, 3)
>>> print(f)
<function lazy_sum.<locals>.sum at 0x10f506158>
>>> f()
6
```

###### 2.2 闭包

> 闭包就是能够读取其他函数内部变量的函数。例如在javascript中，只有函数内部的子函数才能读取局部变量，所以闭包可以理解成“定义在一个函数内部的函数“。在本质上，闭包是将函数内部和函数外部连接起来的桥梁。

举例见 [returnFun.py](returnFun.py)

### 3 匿名函数

在Python中，对匿名函数提供了有限支持。

```
>>> list(map(lambda x:x+x, [1, 2, 3]))
[2, 4, 6]
>>> reduce(lambda x, y: x * y, [1, 2, 3])
6
```

### 4. 装饰器
装饰器的作用就是为已经存在的函数或对象添加额外的功能。

> 装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景，比如：插入日志、性能测试、事务处理、缓存、权限校验等场景。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码并继续重用。

举例见 [decorator.py](decorator.py)

### 5.偏函数

偏函数是将所要承载的函数作为  partial()  函数的第一个参数，原函数的各个参数依次作为  partial()  函数的后续参数，除非使用关键字参数。

```
class partial(builtins.object)
 |  partial(func, *args, **keywords) - new function with partial application
 |  of the given arguments and keywords.
 |  
 |  Methods defined here:
 |  
 |  __call__(self, /, *args, **kwargs)
 |      Call self as a function.
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __reduce__(...)
 |      Helper for pickle.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
```

当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
