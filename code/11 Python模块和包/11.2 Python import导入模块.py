
#http://c.biancheng.net/view/2397.html

'''
import 模块名 as 别名
下面程序使用导入整个模块的最简单语法来导入指定模块：
'''

# 导入sys整个模块
import sys
# 使用sys模块名作为前缀来访问模块中的成员
print(sys.argv[0])


# 导入sys整个模块，并指定别名为s
import sys as s
# 使用s模块别名作为前缀来访问模块中的成员
print(s.argv[0])


# 也可以一次导入多个模块，多个模块之间用逗号隔开。例如如下程序：
# 导入sys、os两个模块
import sys,os
# 使用模块名作为前缀来访问模块中的成员
print(sys.argv[0])
# os模块的sep变量代表平台上的路径分隔符
print(os.sep)


# 在导入多个模块的同时，也可以为模块指定别名，例如如下程序：
# 导入sys、os两个模块，并为sys指定别名s，为os指定别名o
import sys as s,os as o
# 使用模块别名作为前缀来访问模块中的成员
print(s.argv[0])
print(o.sep)


'''from  模块名 import 成员名 as 别名'''
# 下面程序使用了 from...import 最简单的语法来导入指定成员：
# 导入sys模块的argv成员
from sys import argv
# 使用导入成员的语法，直接使用成员名访问
print(argv[0])


# 导入模块成员时，也可以为成员指定别名，例如如下程序：
# 导入sys模块的argv成员，并为其指定别名v
from sys import argv as v
# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
print(v[0])


# form...import 导入模块成员时，支持一次导入多个成员，例如如下程序：
# 导入sys模块的argv,winver成员
from sys import argv, winver
# 使用导入成员的语法，直接使用成员名访问
print(argv[0])
#sys 的 winver 成员记录了该 Python 的版本号
print(winver)


# 一次导入多个模块成员时，也可指定别名，同样使用 as 关键字为成员指定别名，例如如下程序：
# 导入sys模块的argv,winver成员，并为其指定别名v、wv
from sys import argv as v, winver as wv
# 使用导入成员（并指定别名）的语法，直接使用成员的别名访问
print(v[0])
print(wv)


# 不推荐使用 from import 导入模块所有成员
# 在使用 from...import 语法时，可以一次导入指定模块内的所有成员（此方式不推荐），例如如下程序：
#导入sys 棋块内的所有成员
from sys import *
#使用导入成员的语法，直接使用成员的别名访问
print(argv[0])
print(winver)

