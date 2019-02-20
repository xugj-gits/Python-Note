# Python数据类型

![avatar](Python数据类型.png)

### 1.字符串
##### 1.1 使用单引号
用单引号括起来表示字符串，例如：
` str = 'this is python-note' `
##### 1.2 使用双引号
双引号中的字符串与单引号中的字符串用法完全相同，例如：
` str = "this is python-note" `
##### 1.3 使用三引号
利用三引号，表示多行的字符串，可以在三引号中自由的使用单引号和双引号，例如：
```
str='''this is string
this is pythod string
this is string'''
```
##### 1.4 转义字符 '\\'

转义字符 \ 可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\

Python还允许用r''表示''内部的字符串默认不转义

### 2.布尔类型
在Python中，可以直接用True、False表示布尔值 <font color="#dd0000">（请注意大小写）</font>

##### 2.1 and 运算
and运算是与运算，只有所有都为True，and运算结果才是True：
```
>>> True
True
>>> True and True
True
>>> True and False
False
```
##### 2.2 or 运算
or运算是或运算，只要其中有一个为True，or运算结果就是True：
```
>>> True or False
True
>>> True or True
True
>>> False or False
False
>>> 
```
##### 2.3 not 运算
not运算是非运算，它是一个单目运算符，把True变成False，False变成True：
```
>>> not True
False
>>> not False
True
>>> not not True
True
>>> 
```
### 3.整数
Python可以处理任意大小的整数（正负）
```
>>> print(10)
10
>>> print(-1)
-1
>>> 
```
### 4.浮点数
浮点数也就是小数
```
>>> print(1.0)
1.0
>>> print(1.25E20)
1.25e+20
>>> print(1.28e20)
1.28e+20
>>> print(1.28e6)
1280000.0
```
### 5.数字
数字包括整数和浮点数
### 6.列表
Python内置的一种数据类型是列表：list。list是一种<font color="#dd0000">有序</font>的集合，可以随时添加和删除其中的元素。
- 创建列表
```
>>> student = ['张三','李四']
>>> student
['张三', '李四']
```
- 常用函数

    + len获得list元素的个数:
        ```
        >>> len(student)
        2
        ```
    + pop删除list末尾的元素:
        ```
        >>> student.pop()
        '李四'
        >>> student
        ['张三']
        ```
### 7.元组
另一种<font color="#dd0000">有序</font>列表叫元组：tuple。tuple和list非常类似，但是tuple<font color="#dd0000">一旦初始化就不能修改</font>。
```
>>> student = ('张三','李四')
>>> student
('张三', '李四')
```
注意这里定义元组使用的是小括号

### 8.字典
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，<font color="#dd0000">具有极快的查找速度</font>。
```
>>> d = {'小红' : 98, '小李' : 96, '小明' : 86 }
>>> d['小明']
86
```
- dict和list对比

对比|查找|插入|占用内存
--|:--:|:--:|--:
dict|快|快|多
list|元素多就慢|元素多就慢|少

### 9.日期

datetime是Python处理日期和时间的标准库。

1. 获取当前日期和时间
```
>>> from datetime import datetime
>>> now = datetime.now()
>>> print(now)
2019-02-20 17:18:52.923892
```
2. datetime转换为timestamp
```
>>> now.timestamp()
1550654332.923892
```
>注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。需要乘以1000转换为秒

3. timestamp转换为datetime
```
>>> t  = 1550654332.923892
>>> print(datetime.fromtimestamp(t))
2019-02-20 17:18:52.923892
```
4. str转换为datetime
```
>>> dateCurr = datetime.strptime('2019-02-20 17:29:01', '%Y-%m-%d %H:%M:%S')
>>> print(dateCurr)
2019-02-20 17:29:01
```
> %Y-%m-%d %H:%M:%S 注意大小写 [Python日期格式](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior)


