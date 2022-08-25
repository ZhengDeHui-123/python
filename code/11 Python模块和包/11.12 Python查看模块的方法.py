
#查看模块成员：dir()函数
import string
# print(dir(string))
# for i in dir(string):
#     print(i)

#可以看到，通过 dir() 函数获取到的模块成员，不仅包含供外部文件使用的成员，还包含很多“特殊”
# （名称以 2 个下划线开头和结束）的成员，列出这些成员，对我们并没有实际意义。
# 因此，这里给读者推荐一种可以忽略显示 dir() 函数输出的特殊成员的方法。仍以 string 模块为例：
# import string
print([e for e in dir(string) if not e.startswith('_')])

#查看模块成员：__all__变量

# 除了使用 dir() 函数之外，还可以使用 __all__ 变量，借助该变量也可以查看模块（包）内包含的所有成员。
# 仍以 string 模块为例，举个例子：
# import string
print(string.__all__)

# 显然，和 dir() 函数相比，__all__ 变量在查看指定模块成员时，它不会显示模块中的特殊成员，同时还会根据成员的名称进行排序显示。
# 不过需要注意的是，并非所有的模块都支持使用 __all__ 变量，因此对于获取有些模块的成员，就只能使用 dir() 函数。