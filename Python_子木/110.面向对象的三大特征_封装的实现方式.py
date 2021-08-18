'''
接着找对象

课程介绍

1、封装
2、继承
3、方法重写
4、object类
5、多态
6、特殊方法和特殊属性

封装

面向对象的三大特征
    封装：提高程序的安全性
        将数据（属性）和行为（方法）包装到类对象中。在方法内部对属性进行操作，在
        类对象的外部调用方法。这样，无需关心方法内部的具体实现细节，从而隔离了复
        杂度。
        在Python中没有专门的修饰符用于属性的私有，如果该属性不希望在类对象外部被
        访问，前边使用两个”_“。
    继承：提高代码的复用性
    多态：提高程序的可扩展性和可维护性

class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动。。。')

car=Car('宝马X5')
car.start()
print(car.brand)

'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)

stu=Student('张三',20)
stu.show()
#在类的外使用name与age
print(stu.name)
#print(stu.__age)
# print(dir(stu))
print(stu._Student__age)