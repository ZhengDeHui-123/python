#Developer：ZhengDeHui
#Developer Time： 2022/8/3 11:01

# class TheFirstDemo:
#     '''这是一个学习Python定义的第一个类'''
#     #构造方法
#     def __init__(self):
#         print("调用构造方法")
#     # 下面定义了一个类属性
#     add = 'http://c.biancheng.net'
#     # 下面定义了一个say方法
#     def say(self, content):
#         print(content)
#
# zhangsan = TheFirstDemo()


class CLanguage:
    '''这是一个学习Python定义的一个类'''
    def __init__(self,name,add):
        print(name,"的网址为:",add)
#创建 add 对象，并传递参数给构造函数
add = CLanguage("C语言中文网","http://c.biancheng.net")