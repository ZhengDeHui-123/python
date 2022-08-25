
'''
http://c.biancheng.net/view/2547.html
'''

#下面程序演示了如何使用 input() 函数依次读取这 2 个文件：
import fileinput
#使用for循环遍历 fileinput 对象
for line in fileinput.input(files=('my_file.txt', 'file.txt')):
    # 输出读取到的内容
    print(line)
# 关闭文件流
fileinput.close()


#注意，和 open() 函数不同，input() 函数不能指定打开文件的编码格式，这意味着使用该函数读取的所有文件，
# 除非以二进制方式进行读取，否则该文件编码格式都必须和当前操作系统默认的编码格式相同，不然 Python 解
# 释器可能会提示 UnicodeDecodeError 错误。
