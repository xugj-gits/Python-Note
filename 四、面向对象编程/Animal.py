# -*- coding:UTF-8 -*-

# 对于Animal来说，Dog, Cat就是它的子类
class Animal(object):
    
    def run(self):
        print('This is Animal')

# 对于Dog来说，Animal就是它的父类
class Dog(Animal):
    
    def run(self):
        print('Dog is runing...')

# 对于Cat来说，Animal就是它的父类
class Cat(Animal):
    def run(self):
        print('Cat is runing...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()