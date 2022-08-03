#Developer：ZhengDeHui
#Developer Time： 2022/8/3 11:42

# class Person:
#     def __init__(self):
#         print("正在执行构造方法")
#     # 定义一个study()实例方法
#     def study(self,name):
#         print(name,"正在学Python")

# class Person:
#     def __init__(self):
#         print("正在执行构造方法")
#     # 定义一个study()实例方法
#     def study(self):
#         print(self,"正在学Python")
# zhangsan = Person()
# zhangsan.study()
# lisi = Person()
# lisi.study()

# class Person:
#     name = "xxx"
#     def __init__(self,name):
#         self.name=name
# zhangsan = Person("zhangsan")
# print(zhangsan.name)
# lisi = Person("lisi")
# print(lisi.name)


class Person:
    def who(self):
        print(self)
zhangsan = Person()
#第一种方式
zhangsan.who()
#第二种方式
who = zhangsan.who
who()#通过 who 变量调用zhangsan对象中的 who() 方法