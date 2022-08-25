import linecache
import string
#读取string模块中第 3 行的数据
print(linecache.getline(string.__file__, 3))
# 读取普通文件的第2行
print(linecache.getline('my_file.txt', 2))
