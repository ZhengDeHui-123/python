
#http://c.biancheng.net/view/2542.html

from os import path
# 获取绝对路径
print(path.abspath("my_file.txt"))
# 获取共同前缀
print(path.commonprefix(['C://my_file.txt', 'C://a.txt']))
# 获取共同路径
print(path.commonpath(['http://c.biancheng.net/python/', 'http://c.biancheng.net/shell/']))
# 获取目录
print(path.dirname('C://my_file.txt'))
# 判断指定目录是否存在
print(path.exists('my_file.txt'))