#Developer：ZhengDeHui
#Developer Time： 2022/8/3 15:17

class CLanguage:
    def info(self):
        print("我正在学 Python")
#通过类名直接调用实例方法
clang = CLanguage
CLanguage.info(clang)


class CLanguage:
    def info(self):
        print(self,"正在学 Python")
#通过类名直接调用实例方法
CLanguage.info("zhangsan")



