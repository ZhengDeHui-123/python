#Developer：ZhengDeHui
#Developer Time： 2022/8/4 13:57

# class CLanguage:
#     pass
# #下面定义了一个实例方法
# def info(self):
#     print("正在调用实例方法")
# #下面定义了一个类方法
# @classmethod
# def info2(cls):
#     print("正在调用类方法")
# #下面定义个静态方法
# @staticmethod
# def info3():
#     print("正在调用静态方法")
# #类可以动态添加以上 3 种方法，会影响所有实例对象
# CLanguage.info = info
# CLanguage.info2 = info2
# CLanguage.info3 = info3
# clang = CLanguage()
# #如今，clang 具有以上 3 种方法
# clang.info()
# clang.info2()
# clang.info3()
# #类实例对象只能动态添加实例方法，不会影响其它实例对象
# clang1 = CLanguage()
# clang1.info = info
# #必须手动为 self 传值
# clang1.info(clang1)

# class CLanguage:
#     __slots__ = ('name','add','info')

# def info(self,name):
#     print("正在调用实例方法",self.name)
# clang = CLanguage()
# clang.name = "C语言中文网"
# #为 clang 对象动态添加 info 实例方法
# clang.info = info
# clang.info(clang,"Python教程")

#根据 __slots__ 属性的设置，CLanguage 类的实例对象是不能动态添加以 say 为名称的方法的。
# def info(self,name):
#     print("正在调用实例方法",self.name)
# clang = CLanguage()
# clang.name = "C语言中文网"
# clang.say = info
# clang.say(clang,"Python教程")

# def info(self):
#     print("正在调用实例方法")
# CLanguage.say = info
# clang = CLanguage()
# clang.say()

class CLanguage:
    __slots__ = ('name','add','info')
#Clanguage 的空子类
class CLangs(CLanguage):
    pass
#定义的实例方法
def info(self):
    print("正在调用实例方法")
clang = CLangs()
#为子类对象动态添加 say() 方法
clang.say = info
clang.say(clang)