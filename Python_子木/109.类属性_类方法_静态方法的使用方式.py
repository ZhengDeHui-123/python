'''
类属性、类方法、静态方法

类属性：类中方法外的变量称为类属性，被该类的的所有对象所共享
类方法：使用@classmethod修饰的方法，使用类名直接访问的方法
静态方法：使用staticmethod修饰的方法，使用类名直接访问的方法

print(Student.native_place) #访问类属性
Student.cm() #调用类方法
Student.sm() #调用静态方法
'''

class Student:  # Student为类的名称（类名）有一个或多个单词组成，每个单词的首字母大写，其余小写
    native_place = '吉林'  # 类属性

    def __init__(self, name, age):
        self.name = name  # self.name 称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实例属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭。。。')

    # 静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')


#类属性的使用方式
print(Student.native_place)
stu1=Student('张三',20)
stu2=Student('李四',30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place='天津'
print(stu1.native_place)
print(stu2.native_place)
print('----------------类方法的使用方式--------------------')
Student.cm()
print('----------------静态方法的使用方式--------------------')
Student.method()

