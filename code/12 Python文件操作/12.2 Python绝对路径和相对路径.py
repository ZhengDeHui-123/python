import os

# 获取当前目录路径
print(os.getcwd())
#修改目录路径
os.chdir('C:\\Windows\\System32')
print(os.getcwd())

#调用 os.path.abspath(path) 将返回 path 参数的绝对路径的字符串，这是将相对路径转换为绝对路径的简便方法。
print(os.path.abspath('.'))
print(os.path.abspath('.\\Scripts'))

# 调用 os.path.isabs(path)，如果参数是一个绝对路径，就返回 True，如果参数是一个相对路径，就返回 False。
print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))
#替换路径
print(os.path.relpath('C:\\Windows','C:\\'))
#上级目录
print(os.path.relpath('C:\\Windows', 'C:\\spam\\eggs'))
path = 'C:\\Windows\\System32\\calc.exe'

#调用 os.path.basename(path) 将返回一个字符串，它包含 path 参数中最后一个斜杠之后的所有内容。
print(os.path.basename(path))
#调用 os.path.dirname(path) 将返回一个字符串，它包含 path 参数中最后一个斜杠之前的所有内容；
print(os.path.dirname(path))

#如果同时需要一个路径的目录名称和基本名称，就可以调用 os.path.split() 获得这两个字符串的元组，例如：
path = 'C:\\Windows\\System32\\calc.exe'
print(os.path.split(path))

#如果 path 参数所指的文件或文件夹存在，调用 os.path.exists(path) 将返回 True，否则返回 False。
print(os.path.exists('C:\\Windows'))
print(os.path.exists('C:\\some_made_up_folder'))

#如果 path 参数存在，并且是一个文件，调用 os.path.isfile(path) 将返回 True，否则返回 False。
print(os.path.isfile('C:\\Windows\\System32'))
print(os.path.isfile('C:\\Windows\\System32\\calc.exe'))

#如果 path 参数存在，并且是一个文件夹，调用 os.path.isdir(path) 将返回 True，否则返回 False。
print(os.path.isdir('C:\\Windows\\System32'))
print(os.path.isdir('C:\\Windows\\System32\\calc.exe'))




