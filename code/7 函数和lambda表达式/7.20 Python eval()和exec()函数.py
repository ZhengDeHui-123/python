#Developer：ZhengDeHui
#Developer Time： 2022/8/5 14:36

# dic={} #定义一个字典
# dic['b'] = 3 #在 dic 中加一条元素，key 为 b
# print (dic.keys()) #先将 dic 的 key 打印出来，有一个元素 b
# exec("a = 4", dic) #在 exec 执行的语句后面跟一个作用域 dic
# print(dic.keys()) #exec 后，dic 的 key 多了一个


#locals参数的用法就很简单了，举个例子：
# a=10
# b=20
# c=30
# g={'a':6, 'b':8} #定义一个字典
# t={'b':100, 'c':10} #定义一个字典
# print(eval('a+b+c', g, t)) #定义一个字典 116


# exec()和eval()的区别
# 它们的区别在于，eval() 执行完会返回结果，而 exec() 执行完不返回结果。举个例子：
a = 1
exec("a = 2") #相当于直接执行 a=2
print(a)
a = exec("2+3") #相当于直接执行 2+3，但是并没有返回值，a 应为 None
print(a)
a = eval('2+3') #执行 2+3，并把结果返回给 a
print(a)

# a= eval("a = 2")