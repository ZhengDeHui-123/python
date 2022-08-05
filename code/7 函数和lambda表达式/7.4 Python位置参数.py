#Developer：ZhengDeHui
#Developer Time： 2022/8/5 9:48

'''实参和形参数量必须一致'''

#少传参数报错
# def girth(width , height):
#     return 2 * (width + height)
# #调用函数时，必须传递 2 个参数，否则会引发错误
# print(girth(3))

#多传参数报错
# def girth(width , height):
#     return 2 * (width + height)
# #调用函数时，必须传递 2 个参数，否则会引发错误
# print(girth(3,2,4))

#字符串和数值相乘报错
# def area(height,width):
#     return height*width/2
# print(area("C语言中文网",3))

#需求：设计一个求梯形面积的函数，并利用此函数求上底为 4cm，下底为 3cm，高为 5cm 的梯形的面积。
def area(upper_base,lower_bottom,height):
    return (upper_base+lower_bottom)*height/2
print("正确结果为：",area(4,3,5))
print("错误结果为：",area(4,5,3))