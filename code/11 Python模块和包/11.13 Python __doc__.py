
# 在使用 dir() 函数和 __all__ 变量的基础上，虽然我们能知晓指定模块（或包）中所有可用的成员（变量、函数和类），比如：
# import string
# print(string.__all__)

'''
# 现在，我们先借助 dir() 函数，查看 my_package 包中有多少可供我们调用的成员：
import my_package
print([e for e in dir(my_package) if not e.startswith('_')])

# 通过此输出结果可以得知，在 my_package 包中，有以上 4 个成员可供我们使用。接下来，我们使用 help() 函数来查看这些成员的具体含义（以 module1 为例）：
# import my_package
help(my_package.module1)


#输出 module2 成员的具体信息
help(my_package.module2)
#输出 display 成员的具体信息
help(my_package.module1.display)
#输出 CLanguage 成员的具体信息
help(my_package.module2.CLanguage)
'''

#值得一提的是，之所以我们可以使用 help() 函数查看具体成员的信息，是因为该成员本身就包含表示自身身
# 份的说明文档（本质是字符串，位于该成员内部开头的位置）。前面讲过，无论是函数还是类，都可以使用
# __doc__ 属性获取它们的说明文档，模块也不例外。
# 以 my_package 包 module1 模块中的 display() 函数为例，我们尝试用 __doc__ 变量获取其说明文档：
import my_package
print(my_package.module1.display.__doc__)