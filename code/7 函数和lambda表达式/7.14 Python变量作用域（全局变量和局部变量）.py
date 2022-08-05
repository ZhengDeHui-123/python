#Developer：ZhengDeHui
#Developer Time： 2022/8/5 10:40

'''Python局部变量'''

# def demo():
#     add = "http://c.biancheng.net/python/"
#     print("函数内部 add =",add)
# demo()
# print("函数外部 add =",add)

#函数的参数也属于局部变量，只能在函数内部使用。
# def demo(name,add):
#     print("函数内部 name =",name)
#     print("函数内部 add =",add)
# demo("Python教程","http://c.biancheng.net/python/")
# print("函数外部 name =",name)
# print("函数外部 add =",add)


'''Python全局变量'''

# add = "http://c.biancheng.net/shell/"
# def text():
#     print("函数体内访问：",add)
# text()
# print('函数体外访问：',add)

#在函数体内定义全局变量。即使用 global 关键字对变量进行修饰后，该变量就会变为全局变量。例如：

# def text():
#     global add
#     add= "http://c.biancheng.net/java/"
#     print("函数体内访问：",add)
# text()
# print('函数体外访问：',add)


# globals()函数
# globals() 函数为 Python ，它可以返回一个包含全局范围内所有变量的字典，该字典中的每个键值对，键为变量名，值为该变量的值。
#全局变量
# Pyname = "Python教程"
# Pyadd = "http://c.biancheng.net/python/"
# def text():
#     #局部变量
#     Shename = "shell教程"
#     Sheadd= "http://c.biancheng.net/shell/"
# print(globals())
#
#
# print(globals()['Pyname'])
# globals()['Pyname'] = "Python入门教程"
# print(Pyname)


#locals()函数
#全局变量
# Pyname = "Python教程"
# Pyadd = "http://c.biancheng.net/python/"
# def text():
#     #局部变量
#     Shename = "shell教程"
#     Sheadd= "http://c.biancheng.net/shell/"
#     print("函数内部的 locals:")
#     print(locals())
# text()
# print("函数外部的 locals:")
# print(locals())


#全局变量
# Pyname = "Python教程"
# Pyadd = "http://c.biancheng.net/python/"
# def text():
#     #局部变量
#     Shename = "shell教程"
#     Sheadd= "http://c.biancheng.net/shell/"
#     print(locals()['Shename'])
#     locals()['Shename'] = "shell入门教程"
#     print(Shename)
# text()


#vars(object)


 #全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"
class Demo:
    name = "Python 教程"
    add = "http://c.biancheng.net/python/"
print("有 object：")
print(vars(Demo))
print("无 object：")
print(vars())