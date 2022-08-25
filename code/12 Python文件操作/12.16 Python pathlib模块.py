# PurePath 类的用法

from pathlib import *
# 创建PurePath，实际上使用PureWindowsPath
path = PurePath('my_file.txt')
print(type(path))


'''除此之外，PurePath 在创建对象时，也支持传入多个路径字符串，它们会被拼接成一个路径格式的字符串。例如：'''
from pathlib import *
# 创建PurePath，实际上使用PureWindowsPath
path = PurePath('http:','c.biancheng.net','python')
print(path)


'''
可以看到，由于本机为 Windows 系统，因此这里输出的是适用于 Windows 平台的路径。
如果想在 Windows 系统上输出 UNIX 风格的路径字符串，就需要使用 PurePosixPath 类。例如：
'''
from pathlib import *
path = PurePosixPath('http:','c.biancheng.net','python')
print(path)

'''
值的一提的是，如果在使用 PurePath 类构造方法时，不传入任何参数，则等同于传入点‘.’（表示当前路径）作为参数。例如：
'''
from pathlib import *
path = PurePath()
print(path)
path = PurePath('.')
print(path)


'''
另外，如果传入 PurePath 构造方法中的多个参数中，包含多个根路径，则只会有最后一个根路径及后面的子路径生效。例如：
'''

from pathlib import *
path = PurePath('C://','D://','my_file.txt')
print(path)

#注意，对于 Windows 风格的路径，只有盘符（如 C、D等）才能算根路径。

# 需要注意的是，如果传给 PurePath 构造方法的参数中包含有多余的斜杠或者点（ . ，表示当前路径），会直接被忽略（ .. 不会被忽略）。举个例子：
from pathlib import *
path = PurePath('C://./my_file.txt')
print(path)


'''
PurePath 类还重载各种比较运算符，多余同种风格的路径字符串来说，可以判断是否相等，也可以比较大小
（实际上就是比较字符串的大小）；对于不同种风格的路径字符串之间，只能判断是否相等（显然，不可能相等）
，但不能比较大小。

举个例子：
'''
from pathlib import *
# Unix风格的路径区分大小写
print(PurePosixPath('C://my_file.txt') == PurePosixPath('c://my_file.txt'))
# Windows风格的路径不区分大小写
print(PureWindowsPath('C://my_file.txt') == PureWindowsPath('c://my_file.txt'))

#比较特殊的是，PurePath 类对象支持直接使用斜杠（/）作为多个字符串之间的连接符，例如：
from pathlib import *
path = PurePosixPath('C://')
print(path / 'my_file.txt')


#通过以上方式构建的路径，其本质上就是字符串，因此我们完全可以使用 str() 将 PurePath 对象转换成字符串。例如：
from pathlib import *
# Unix风格的路径区分大小写
path = PurePosixPath('C://','my_file.txt')
print(str(path))

#http://c.biancheng.net/view/2541.html