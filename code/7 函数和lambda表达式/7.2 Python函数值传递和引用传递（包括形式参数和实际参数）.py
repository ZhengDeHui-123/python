#Developer：ZhengDeHui
#Developer Time： 2022/8/4 17:06

#定义函数时，这里的函数参数 obj 就是形式参数
def demo(obj):
    print(obj)

a = "C语言中文网"
#调用已经定义好的 demo 函数，此时传入的函数参数 a 就是实际参数
demo(a)


def demo(obj) :
    obj += obj
    print("形参值为：",obj)
print("-------值传递-----")
a = "C语言中文网"
print("a的值为：",a)
demo(a)
print("实参值为：",a)
print("-----引用传递-----")
a = [1,2,3]
print("a的值为：",a)
demo(a)
print("实参值为：",a)