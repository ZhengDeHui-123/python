#Developer：ZhengDeHui
#Developer Time： 2022/8/4 15:30

# from enum import Enum
# class Color(Enum):
#     # 为序列值指定value值
#     red = 1
#     green = 2
#     blue = 3
#
# #调用枚举成员的 3 种方式
# print(Color.red)
# print(Color['red'])
# print(Color(1))
# #调取枚举成员中的 value 和 name
# print(Color.red.value)
# print(Color.red.name)
# #遍历枚举类中所有成员的 2 种方式
# for color in Color:
#     print(color)
#
# #枚举类成员之间不能比较大小，但可以用 == 或者 is 进行比较是否相等，例如：
# print(Color.red == Color.green)
# print(Color.red.name is Color.green.name)

#需要注意的是，枚举类中各个成员的值，不能在类的外部做任何修改，也就是说，下面语法的做法是错误的：
#Color.red = 4

# for name,member in Color.__members__.items():
#     print(name,"->",member)


# from enum import Enum
# class Color(Enum):
#     # 为序列值指定value值
#     red = 1
#     green = 1
#     blue = 3
# print(Color['green'])

#引入 unique
# from enum import Enum,unique
# #添加 unique 装饰器
# @unique
# class Color(Enum):
#     # 为序列值指定value值
#     red = 1
#     green = 1
#     blue = 3
# print(Color['green'])


from enum import Enum
#创建一个枚举类
Color = Enum("Color",('red','green','blue'))
#调用枚举成员的 3 种方式
print(Color.red)
print(Color['red'])
print(Color(1))
#调取枚举成员中的 value 和 name
print(Color.red.value)
print(Color.red.name)
#遍历枚举类中所有成员的 2 种方式
for color in Color:
    print(color)