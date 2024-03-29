#Developer：ZhengDeHui
#Developer Time： 2022/8/4 14:40

#定义一个元类
class FirstMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 动态为该类添加一个name属性
        attrs['name'] = "C语言中文网"
        attrs['say'] = lambda self: print("调用 say() 实例方法")
        return super().__new__(cls,name,bases,attrs)


#定义类时，指定元类
class CLanguage(object,metaclass=FirstMetaClass):
    pass
clangs = CLanguage()
print(clangs.name)
clangs.say()