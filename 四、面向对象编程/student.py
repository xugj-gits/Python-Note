# -*_ coding: UTF-8 -*-

class Student:
    def __init__(self, name, score, gender):
        self.name = name
        self.score = score
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59, '男')
lisa = Student('Lisa Simpson', 87, '女')

print('bart.name=', bart.name)
print('bart.score=', bart.score)

bart.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())

# 不建议这样使用
bart._Student__gender

# 会报错：'Student' object has no attribute '__gender'
# bart.__gender



print('gender of Bart:', bart.get_gender())