'''
动态绑定属性和方法

Python是动态语言，在创建对象之后，可以动态的绑定属性和方法

    def show():
        print('我是一函数')

    stu=Student('Jack',20)
    stu.gender='男' #动态绑定性别
    print(stu.name,stu.age,stu.gender)
    stu.show=show #动态绑定方法
    stu.show()
'''

class Student:  # Student为类的名称（类名）有一个或多个单词组成，每个单词的首字母大写，其余小写

    def __init__(self, name, age):
        self.name = name  # self.name 称为实例属性，进行了一个赋值的操作，将局部变量的name的值赋给实例属性
        self.age = age    #self.age 可以任意去改变，但是习惯上我们让她们相同
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',20) #stu1 实例对象、Student 类对象
stu2=Student('李四',30)
print(id(stu1))
print(id(stu2))
print('----------------为stu1动态绑定性别属性--------------------')
stu1.gender='女'
print(stu1.name,stu1.age,stu1.gender)
print(stu2.name,stu2.age)

print('------------------------------')
stu1.eat()
stu2.eat()

def show():
    print('定义在类之外的称为函数')

stu1.show = show #绑定到对象上，就称为方法
stu1.show()

#一个Student类可以创建N多个Student类的实例对象，每个实例对象的属性值不同

#stu2.show() #因为stu2并没有绑定show方法

'''
知识点总结

            面向过程
    编程思想 
            面向对象
                                        类名() 创建实例对象
                               实例      动态绑定属性 
                               对象      动态绑定方法 
     
            类属性
    类对象   类方法
    class   实例方法
            静态方法
            
            
'''