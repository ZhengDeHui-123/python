#Developer：ZhengDeHui
#Developer Time： 2022/8/5 11:15


'''例如，计算一个数的 n 次幂，用闭包可以写成下面的代码：'''
#闭包函数，其中 exponent 称为自由变量
# def nth_power(exponent):
#     def exponent_of(base):
#         return base ** exponent
#     return exponent_of # 返回值是 exponent_of 函数
# square = nth_power(2) # 计算一个数的平方
# cube = nth_power(3) # 计算一个数的立方
# print(square(2))  # 计算 2 的平方
# print(cube(2)) # 计算 2 的立方

#为什么要闭包呢？上面的程序，完全可以写成下面的形式：
def nth_power_rewrite(base, exponent):
    return base ** exponent

#上面程序确实可以实现相同的功能，不过使用闭包，可以让程序变得更简洁易读。设想一下，比如需要计算很多个数的平方，那么读者觉得写成下面哪一种形式更好呢？
# 不使用闭包
# res1 = nth_power_rewrite(base1, 2)
# res2 = nth_power_rewrite(base2, 2)
# res3 = nth_power_rewrite(base3, 2)
# # 使用闭包
# square = nth_power(2)
# res1 = square(base1)
# res2 = square(base2)
# res3 = square(base3)


'''Python闭包的__closure__属性'''

def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of
square = nth_power(2)
#查看 __closure__ 的值
print(square.__closure__)



