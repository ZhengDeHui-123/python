#Developer：ZhengDeHui
#Developer Time： 2022/8/4 14:47

'''
a 可以被先后赋值为 CLanguage 类和 CPython 类的对象，但这并不是多态。类的多态特性，还要满足以下 2 个前提条件：
1.继承：多态一定是发生在子类和父类之间；
2.重写：子类重写了父类的方法。
'''

# class CLanguage:
#     def say(self):
#         print("赋值的是 CLanguage 类的实例对象")
# class CPython:
#     def say(self):
#         print("赋值的是 CPython 类的实例对象")
# a = CLanguage()
# a.say()
# a = CPython()
# a.say()

#CPython 和 CLinux 都继承自 CLanguage 类，且各自都重写了父类的 say() 方法。从运行结果可以看出，同一变量 a 在执行同一个 say() 方法时，由于 a 实际表示不同的类实例对象，因此 a.say() 调用的并不是同一个类中的 say() 方法，这就是多态。
# class CLanguage:
#     def say(self):
#         print("调用的是 Clanguage 类的say方法")
# class CPython(CLanguage):
#     def say(self):
#         print("调用的是 CPython 类的say方法")
# class CLinux(CLanguage):
#     def say(self):
#         print("调用的是 CLinux 类的say方法")
# a = CLanguage()
# a.say()
# a = CPython()
# a.say()
# a = CLinux()
# a.say()



class WhoSay:
    def say(self,who):
        who.say()
class CLanguage:
    def say(self):
        print("调用的是 Clanguage 类的say方法")
class CPython(CLanguage):
    def say(self):
        print("调用的是 CPython 类的say方法")
class CLinux(CLanguage):
    def say(self):
        print("调用的是 CLinux 类的say方法")
a = WhoSay()
#调用 CLanguage 类的 say() 方法
a.say(CLanguage())
#调用 CPython 类的 say() 方法
a.say(CPython())
#调用 CLinux 类的 say() 方法
a.say(CLinux())