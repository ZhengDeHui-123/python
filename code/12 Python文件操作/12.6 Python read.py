
# read() 函数：逐个字节或者字符读取文件中的内容；
# readline() 函数：逐行读取文件中的内容；
# readlines() 函数：一次性读取文件中多行内容。

#以 utf-8 的编码格式打开指定文件
f = open("my_file.txt",encoding = "utf-8")
#输出读取到的数据
print(f.read())
#关闭文件
f.close()


#可以通过使用 size 参数，指定 read() 每次可读取的最大字符（或者字节）数，例如：
#以 utf-8 的编码格式打开指定文件
f = open("my_file.txt",encoding = "utf-8")
#输出读取到的数据
print(f.read(6))
#关闭文件
f.close()


#以二进制形式打开指定文件
f = open("my_file.txt",'rb+')
#输出读取到的数据
print(f.read())
#关闭文件
f.close()


#以二进制形式打开指定文件，该文件编码格式为 utf-8
f = open("my_file.txt",'rb+')
byt = f.read()
print(byt)
print("\n转换后：")
print(byt.decode('utf-8'))
#关闭文件
f.close()