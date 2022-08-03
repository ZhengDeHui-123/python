#Developer：ZhengDeHui
#Developer Time： 2022/8/3 15:40

# class CLanguage:
#     #构造函数
#     def __init__(self,name):
#         self.name = name
#     #设置 name 属性值的函数
#     def setname(self,name):
#         self.name = name
#     #访问nema属性值的函数
#     def getname(self):
#         return self.name
#     #删除name属性值的函数
#     def delname(self):
#         self.name="xxx"
# clang = CLanguage("C语言中文网")
# #获取name属性值
# print(clang.getname())
# #设置name属性值
# clang.setname("Python教程")
# print(clang.getname())
# #删除name属性值
# clang.delname()
# print(clang.getname())


'''修改上面的程序，为 name 属性配置 property() 函数：'''
class CLanguage:
    #构造函数
    def __init__(self,n):
        self.__name = n
    #设置 name 属性值的函数
    def setname(self,n):
        self.__name = n
    #访问nema属性值的函数
    def getname(self):
        return self.__name
    #删除name属性值的函数
    def delname(self):
        self.__name="xxx"
    #为name 属性配置 property() 函数
    name = property(getname, setname, delname, '指明出处')
#调取说明文档的 2 种方式
#print(CLanguage.name.__doc__)
help(CLanguage.name)
clang = CLanguage("C语言中文网")
#调用 getname() 方法
print(clang.name)
#调用 setname() 方法
clang.name="Python教程"
print(clang.name)
#调用 delname() 方法
del clang.name
print(clang.name)

# name = property(getname, setname) #name属性可读、可写、不能删除
# name = property(getname)    # name 属性可读，不可写，也不能删除
# name = property(getname, setname,delname)    #name属性可读、可写、也可删除，就是没有说明文档