#Developer：ZhengDeHui
#Developer Time： 2022/8/3 15:04

'''Python类实例方法'''

# class CLanguage:
#     #类构造方法，也属于实例方法
#     def __init__(self):
#         self.name = "C语言中文网"
#         self.add = "http://c.biancheng.net"
#     # 下面定义了一个say实例方法
#     def say(self):
#         print("正在调用 say() 实例方法")
#
# # clang = CLanguage()
# # clang.say()
#
# #类名调用实例方法，需手动给 self 参数传值
# clang = CLanguage()
# CLanguage.say(clang)


'''Python类方法'''

# class CLanguage:
#     #类构造方法，也属于实例方法
#     def __init__(self):
#         self.name = "C语言中文网"
#         self.add = "http://c.biancheng.net"
#     #下面定义了一个类方法
#     @classmethod
#     def info(cls):
#         print("正在调用类方法",cls)
#
# #使用类名直接调用类方法
# CLanguage.info()
# #使用类对象调用类方法
# clang = CLanguage()
# clang.info()


'''Python类静态方法'''

class CLanguage:
    @staticmethod
    def info(name,add):
        print(name,add)

#使用类名直接调用静态方法
CLanguage.info("C语言中文网","http://c.biancheng.net")
#使用类对象调用静态方法
clang = CLanguage()
clang.info("Python教程","http://c.biancheng.net/python")


