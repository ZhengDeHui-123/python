#Developer：ZhengDeHui
#Developer Time： 2022/8/5 11:04

#全局函数
# def outdef ():
#     #局部函数
#     def indef():
#         print("http://c.biancheng.net/python/")
#     #调用局部函数
#     indef()
# #调用全局函数
# outdef()


#全局函数
# def outdef ():
#     #局部函数
#     def indef():
#         print("调用局部函数")
#     #调用局部函数
#     return indef
# #调用全局函数
# new_indef = outdef()
# # 调用全局函数中的局部函数
# new_indef()

#全局函数
# def outdef ():
#     name = "所在函数中定义的 name 变量"
#     #局部函数
#     def indef():
#         print(name)
#         name = "局部函数中定义的 name 变量"
#     indef()
# #调用全局函数
# outdef()


#全局函数
def outdef ():
    name = "所在函数中定义的 name 变量"
    #局部函数
    def indef():
        nonlocal name
        print(name)
        #修改name变量的值
        name = "局部函数中定义的 name 变量"
    indef()
#调用全局函数
outdef()