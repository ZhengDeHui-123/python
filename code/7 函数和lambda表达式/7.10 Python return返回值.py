#Developer：ZhengDeHui
#Developer Time： 2022/8/5 10:32

def add(a,b):
    c = a + b
    return c
#函数赋值给变量
c = add(3,4)
print(c)
#函数返回值作为其他函数的实际参数
print(add(3,4))

#们在调用函数时，既可以将该函数赋值给一个变量，用变量保存函数的返回值，也可以将函数再作为某个函数的实际参数。
def isGreater0(x):
    if x > 0:
        return True
    else:
        return False
print(isGreater0(5))
print(isGreater0(0))