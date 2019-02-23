# Python-Note

python中的一些查询模块、函数等使用方法的操作

- help()
    ```
    >>> help(abs)
    Help on built-in function abs in module builtins:

    abs(x, /)
        Return the absolute value of the argument.
    (END)
    ```

- dir() 列出所查询内容的内置属性和方法
    ```
    >>> dir(abs)
    ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']
    ```

- \_\_doc__ 一般为创建该类时候的备注
    ```
    >>> abs.__doc__
    'Return the absolute value of the argument.'
    ```

- \_\_dict__ 查看对象所拥有的属性