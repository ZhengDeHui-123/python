#Developer：ZhengDeHui
#Developer Time： 2022/8/5 10:18

#str1没有默认参数，str2有默认参数
def dis_str(str1,str2 = "http://c.biancheng.net/python/"):
    print("str1:",str1)
    print("str2:",str2)
dis_str("http://c.biancheng.net/shell/")
dis_str("http://c.biancheng.net/java/","http://c.biancheng.net/golang/")

#结合关键字参数，以下 3 种调用 dis_str() 函数的方式也是可以的：
dis_str(str1 = "http://c.biancheng.net/shell/")
dis_str("http://c.biancheng.net/java/",str2 = "http://c.biancheng.net/golang/")
dis_str(str1 = "http://c.biancheng.net/java/",str2 = "http://c.biancheng.net/golang/")

#当定义一个有默认值参数的函数时，有默认值的参数必须位于所有没默认值参数的后面
#语法错误
# def dis_str(str1="http://c.biancheng.net/python/",str2,str3):
#     pass

print(dis_str.__defaults__)