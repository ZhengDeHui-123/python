name = "Python教程"
add = "http://c.biancheng.net/python"
print(name,add)
def say():
    print("人生苦短，我学Python！")
class CLanguage:
    def __init__(self,name,add):
        self.name = name
        self.add = add
    def say(self):
        print(self.name,self.add)

#但通常情况下，为了检验模板中代码的正确性，我们往往需要为其设计一段测试代码，例如：
say()
clangs = CLanguage("C语言中文网","http://c.biancheng.net")
clangs.say()