#Developer：ZhengDeHui
#Developer Time： 2022/8/3 11:12

class CLanguage :
    # 下面定义了2个类变量
    name = "C语言中文网"
    add = "http://c.biancheng.net"
    def __init__(self,name,add):
        #下面定义 2 个实例变量
        self.name = name
        self.add = add
        print(name,"网址为：",add)
    # 下面定义了一个say实例方法
    def say(self, content):
        print(content)
# 将该CLanguage对象赋给clanguage变量
clanguage = CLanguage("C语言中文网","http://c.biancheng.net")


#输出name和add实例变量的值
print(clanguage.name,clanguage.add)
#修改实例变量的值
clanguage.name="Python教程"
clanguage.add="http://c.biancheng.net/python"
#调用clanguage的say()方法
clanguage.say("人生苦短，我用Python")
#再次输出name和add的值
print(clanguage.name,clanguage.add)

# 为clanguage对象增加一个money实例变量
clanguage.money= 159.9
print(clanguage.money)

'''
#删除新添加的 money 实例变量
del clanguage.money
#再次尝试输出 money，此时会报错
print(clanguage.money)
'''


# 先定义一个函数
def info(self):
    print("---info函数---", self)
# 使用info对clanguage的foo方法赋值（动态绑定方法）
clanguage.foo = info
# Python不会自动将调用者绑定到第一个参数，
# 因此程序需要手动将调用者绑定为第一个参数
clanguage.foo(clanguage)  # ①
# 使用lambda表达式为clanguage对象的bar方法赋值（动态绑定方法）
clanguage.bar = lambda self: print('--lambda表达式--', self)
clanguage.bar(clanguage) # ②


def info(self,content):
    print("C语言中文网地址为：%s" % content)
# 导入MethodType
from types import MethodType
clanguage.info = MethodType(info, clanguage)
# 第一个参数已经绑定了，无需传入
clanguage.info("http://c.biancheng.net")