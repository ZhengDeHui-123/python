#Developer：ZhengDeHui
#Developer Time： 2022/8/3 16:46

# class Bird:
#     #鸟有翅膀
#     def isWing(self):
#         print("鸟有翅膀")
#     #鸟会飞
#     def fly(self):
#         print("鸟会飞")
#
# class Ostrich(Bird):
#     # 重写Bird类的fly()方法
#     def fly(self):
#         print("鸵鸟不会飞")


# class Bird:
#     #鸟有翅膀
#     def isWing(self):
#         print("鸟有翅膀")
#     #鸟会飞
#     def fly(self):
#         print("鸟会飞")
# class Ostrich(Bird):
#     # 重写Bird类的fly()方法
#     def fly(self):
#         print("鸵鸟不会飞")
# # 创建Ostrich对象
# ostrich = Ostrich()
# #调用 Ostrich 类中重写的 fly() 类方法
# ostrich.fly()

'''如何调用被重写的方法'''

class Bird:
    #鸟有翅膀
    def isWing(self):
        print("鸟有翅膀")
    #鸟会飞
    def fly(self):
        print("鸟会飞")
class Ostrich(Bird):
    # 重写Bird类的fly()方法
    def fly(self):
        print("鸵鸟不会飞")
# 创建Ostrich对象
ostrich = Ostrich()
#调用 Bird 类中的 fly() 方法
Bird.fly(ostrich)

