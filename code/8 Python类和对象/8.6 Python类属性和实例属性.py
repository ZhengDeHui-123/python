#Developer：ZhengDeHui
#Developer Time： 2022/8/3 14:03

# class CLanguage :
#     # 下面定义了2个类变量
#     name = "C语言中文网"
#     add = "http://c.biancheng.net"
#     # 下面定义了一个say实例方法
#     def say(self, content):
#         print(content)

'''类属性'''
# #使用类名直接调用
# print(CLanguage.name)
# print(CLanguage.add)
# #修改类变量的值
# CLanguage.name = "Python教程"
# CLanguage.add = "http://c.biancheng.net/python"
# print(CLanguage.name)
# print(CLanguage.add)


# clang = CLanguage()
# print(clang.name)
# print(clang.add)

# print("修改前，各类对象中类变量的值：")
# clang1 = CLanguage()
# print(clang1.name)
# print(clang1.add)
# clang2 = CLanguage()
# print(clang2.name)
# print(clang2.add)
# print("修改后，各类对象中类变量的值：")
# CLanguage.name = "Python教程"
# CLanguage.add = "http://c.biancheng.net/python"
# print(clang1.name)
# print(clang1.add)
# print(clang2.name)
# print(clang2.add)

#动态地为类和对象添加类变量
# clang = CLanguage()
# CLanguage.catalog = 13
# print(clang.catalog)

'''实例属性'''

# class CLanguage :
#     def __init__(self):
#         self.name = "C语言中文网"
#         self.add = "http://c.biancheng.net"
#     # 下面定义了一个say实例方法
#     def say(self):
#         self.catalog = 13

# clang = CLanguage()
# print(clang.name)
# print(clang.add)
# #由于 clang 对象未调用 say() 方法，因此其没有 catalog 变量，下面这行代码会报错
# #print(clang.catalog)
# clang2 = CLanguage()
# print(clang2.name)
# print(clang2.add)
# #只有调用 say()，才会拥有 catalog 实例变量
# clang2.say()
# print(clang2.catalog)



# class CLanguage :
#     name = "xxx"  #类变量
#     add = "http://"  #类变量
#     def __init__(self):
#         self.name = "C语言中文网"   #实例变量
#         self.add = "http://c.biancheng.net"   #实例变量
#     # 下面定义了一个say实例方法
#     def say(self):
#         self.catalog = 13  #实例变量
# clang = CLanguage()
# #修改 clang 对象的实例变量
# clang.name = "python教程"
# clang.add = "http://c.biancheng.net/python"
# print(clang.name)
# print(clang.add)
# clang2 = CLanguage()
# print(clang2.name)
# print(clang2.add)
# #输出类变量的值
# print(CLanguage.name)
# print(CLanguage.add)
#
# clang.money = 30
# print(clang.money)

'''局部变量'''

class CLanguage :
    # 下面定义了一个say实例方法
    def count(self,money):
        sale = 0.8*money
        print("优惠后的价格为：",sale)
clang = CLanguage()
clang.count(100)





