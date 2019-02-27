# 面向对象编程
 
 <div align=center><img src="面向对象编程.png"/></div>


### 1. 类和实例

面向对象最重要的概念就是类（Class）和实例（Instance），<font color=red>类是抽象的模板， 实例是根据类创建出来的一个个具体的“对象”</font>

在python中，用变量表示特征，用函数表示技能，因而具有相同特征和技能的一类事物就是‘类’，对象是则是这一类事物中具体的一个。

- 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
- 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
- 数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
- 方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
- 局部变量：定义在方法中的变量，只作用于当前实例的类。
- 实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
- 继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
- 实例化：创建一个类的实例，类的具体对象。
- 方法：类中定义的函数。
- 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

> 使用class语句创建一个新类，class之后为类的名称并以冒号结尾

```
>>> class Student:
...     pass
... 
>>> bart = Student()
>>> bart
<__main__.Student object at 0x10fe359b0>
>>> Student
<class '__main__.Student'>
```

举例[student.py](student.py)

### 2. 访问限制

 * 要让内部属性不被外部访问，可以把属性的名称前加上两个下划线"\__"，在Python中，实例的变量名如果以"__"开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
 <br/>
 * 在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

 在[student.py](student.py)添加了私有变量gender

 ### 3. 继承和多态

 在OOP（Object Oriented Programming）程序设计中，当我们定义一个class的时候，可以从某个现有的class 继承，新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。

 - 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

 - 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

 举例 [Animal.py](Animal.py)

 ### 4. 获取对象信息

 ###### 4.1 type()判断对象类型
 ```
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<class 'NoneType'>
 ```
###### 4.2 isinstance()

```
>>> isinstance(123, int)
True
>>> isinstance('str', str)
True
>>> isinstance(b'a', bytes)
True
```
###### 4.3 dir()

如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
```
>>> dir(123)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```
### 5. 实例属性和类属性

由于Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量

```
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
# 通过实例方法绑定属性
s.score = 90
```
> 在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。


