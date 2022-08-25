# import my_package.module1
# my_package.module1.display("http://c.biancheng.net/java/")
#
# #可以看到，通过此语法格式导入包中的指定模块后，在使用该模块中的成员（变量、函数、类）时，
# # 需添加“包名.模块名”为前缀。当然，如果使用 as 给包名.模块名”起一个别名的话，就使用直接
# # 使用这个别名作为前缀使用该模块中的方法了，例如：
# import my_package.module1 as module
# module.display("http://c.biancheng.net/python/")

#另外，当直接导入指定包时，程序会自动执行该包所对应文件夹下的 __init__.py 文件中的代码。例如：
# import my_package
# my_package.module1.display("http://c.biancheng.net/linux_tutorial/")

import my_package
print(my_package)
print(my_package.__doc__)
print(type(my_package))


# 2) from 包名 import 模块名 [as 别名]
# 仍以导入 my_package 包中的 module1 模块为例，使用此语法格式的实现代码如下：
from my_package import module1
module1.display("http://c.biancheng.net/golang/")


# 3) from 包名.模块名 import 成员名 [as 别名]
# 此语法格式用于向程序中导入“包.模块”中的指定成员（变量、函数或类）。通过该方式导入的变量（函数、类），在使用时可以直接使用变量名（函数名、类名）调用，例如：
from my_package.module1 import display
display("http://c.biancheng.net/shell/")


# 当然，也可以使用 as 为导入的成员起一个别名，例如：
from my_package.module1 import display as dis
dis("http://c.biancheng.net/shell/")

# 另外，在使用此种语法格式加载指定包的指定模块时，可以使用 * 代替成员名，表示加载该模块下的所有成员。例如：
from my_package.module1 import *
display("http://c.biancheng.net/python")


