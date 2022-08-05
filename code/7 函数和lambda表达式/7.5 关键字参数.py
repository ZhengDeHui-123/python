#Developer：ZhengDeHui
#Developer Time： 2022/8/5 10:11

def dis_str(str1,str2):
    print("str1:",str1)
    print("str2:",str2)
#位置参数
dis_str("http://c.biancheng.net/python/","http://c.biancheng.net/shell/")
#关键字参数
dis_str("http://c.biancheng.net/python/",str2="http://c.biancheng.net/shell/")
dis_str(str2="http://c.biancheng.net/python/",str1="http://c.biancheng.net/shell/")


# 位置参数必须放在关键字参数之前，下面代码错误
# dis_str(str1="http://c.biancheng.net/python/","http://c.biancheng.net/shell/")