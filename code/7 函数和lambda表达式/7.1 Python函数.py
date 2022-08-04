#Developer：ZhengDeHui
#Developer Time： 2022/8/4 15:48

n=0
for c in "http://c.biancheng.net/python/":
   n = n + 1
print(n)

#自定义 len() 函数
def my_len(str):
    length = 0
    for c in str:
       length = length + 1
    return length
#调用自定义的 my_len() 函数
length = my_len("http://c.biancheng.net/python/")
print(length)
#再次调用 my_len() 函数
length = my_len("http://c.biancheng.net/shell/")
print(length)


#定义个空函数，没有实际意义
def pass_dis():
    pass
#定义一个比较字符串大小的函数
def str_max(str1,str2):
    str = str1 if str1 > str2 else str2
    return str

print(str_max(10,20))

#函数中的 return 语句可以直接返回一个表达式的值
def str_max(str1,str2):
    return str1 if str1 > str2 else str2


pass_dis()
strmax = str_max("http://c.biancheng.net/python","http://c.biancheng.net/shell");
print(strmax)

#为函数提供说明文档

#定义一个比较字符串大小的函数
def str_max(str1,str2):
    '''
    比较 2 个字符串的大小
    '''
    str = str1 if str1 > str2 else str2
    return str
help(str_max)
#print(str_max.__doc__)
