#Developer：ZhengDeHui
#Developer Time： 2022/8/4 14:34

#查看 3.4 的类型
print(type(3.4))
#查看类对象的类型
class CLanguage:
    pass
clangs = CLanguage()
print(type(clangs))


#定义一个实例方法
def say(self):
    print("我要学 Python！")
#使用 type() 函数创建类
#此程序中通过 type() 创建了类，其类名为 CLanguage，继承自 objects 类，且该类中还包含一个 say() 方法和一个 name 属性。
CLanguage = type("CLanguage",(object,),dict(say = say, name = "C语言中文网"))
#创建一个 CLanguage 实例对象
clangs = CLanguage()
#调用 say() 方法和 name 属性
clangs.say()
print(clangs.name)