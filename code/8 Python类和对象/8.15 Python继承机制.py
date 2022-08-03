#Developer：ZhengDeHui
#Developer Time： 2022/8/3 16:30

'''笨方法 复制代码'''
# class Shape:
#     def draw(self,content):
#         print("画",content)
# class Form:
#     def draw(self,content):
#         print("画",content)
#     def area(self):
#         #....
#         print("此图形的面积为...")

'''继承另外一个类的方法'''
# class Shape:
#     def draw(self,content):
#         print("画",content)
# class Form(Shape):
#     def area(self):
#         #....
#         print("此图形的面积为...")


# class People:
#     def say(self):
#         print("我是一个人，名字是：",self.name)
# class Animal:
#     def display(self):
#         print("人也是高级动物")
# #同时继承 People 和 Animal 类
# #其同时拥有 name 属性、say() 和 display() 方法
# class Person(People, Animal):
#     pass
# zhangsan = Person()
# zhangsan.name = "张三"
# zhangsan.say()
# zhangsan.display()

#子类拥有父类所有的属性和方法，即便该属性或方法是私有（private）的。

'''Python的多继承'''
#注意：使用多继承经常需要面临的问题是，多个父类中包含同名的类方法。对于这种情况，Python 的处置措施是：根据子类继承多个父类时这些父类的前后次序决定，即排在前面父类中的类方法会覆盖排在后面父类中的同名类方法。
class People:
    def __init__(self):
        self.name = People
    def say(self):
        print("People类",self.name)
class Animal:
    def __init__(self):
        self.name = Animal
    def say(self):
        print("Animal类",self.name)
#People中的 name 属性和 say() 会遮蔽 Animal 类中的
class Person(People, Animal):
    pass
zhangsan = Person()
zhangsan.name = "张三"
zhangsan.say()