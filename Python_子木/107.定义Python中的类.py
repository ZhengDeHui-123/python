'''
类的创建

创建类的语法
class Student: #Student为类的名称（类名）有一个或多个单词组成，每个单词的首字母大写，其余小写
    pass

#python中一切皆对象Student是对象吗？内存有空间吗？

print(id(Student)) #2623067335368
print(type(Student)) #<class 'type'>
print(Student) #<class '__main__.Student'>
类的组成
    类属性
    实例方法
    静态方法
    类方法



class Student:
    native_place='吉林' #类属性
    def __init__(self,name,age): #name,age为实例属性
        self.name=name
        self.age=age

    #实例方法
    def info(self):
        print('我的名字叫',self.name,'年龄是:',self.sge)
    #类方法
    @classmethod
    def cm(cls):
        print('类方法')
    #静态方法
    @staticmethod
    def sm():
        print('静态方法')

'''

class Student: #Student为类的名称（类名）有一个或多个单词组成，每个单词的首字母大写，其余小写
    native_place='吉林' #类属性
    def __init__(self,name,age):
        self.name=name #self.name 称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实例属性
        self.age=age


    #实例方法
    def eat(self):
        print('学生在吃饭。。。')

    #静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
        
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')


#在类之外定义的称为函数，在类之内定义的称为方法

def drink():
    print('喝水')