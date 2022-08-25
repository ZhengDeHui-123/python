

'''
事实上，当我们向文件导入某个模块时，导入的是该模块中那些名称不以下划线（单下划线“_”或者双下划线“__”）
开头的变量、函数和类。因此，如果我们不想模块文件中的某个成员被引入到其它文件中使用，可以在其名称前添加下划线。
'''
# 前面章节中创建的 demo.py 模块文件和 test.py 文件为例（它们位于同一目录），各自包含的内容如下所示：

#test.py
# from demo import *
# say()
# CLanguage()
# disPython()


'''Python模块__all__变量'''

# import demo
# demo.say()
# demo.CLanguage()
# demo.disPython()


# 2) 以“from 模块名 import 成员”的形式直接导入指定成员。使用此方式导入的模块，__all__ 变量即便设置，也形同虚设。
# 仍以 demo.py 和 test.py 为例，修改 test.py 文件中的代码，如下所示：

from demo import say
from demo import CLanguage
from demo import disPython
say()
CLanguage()
disPython()