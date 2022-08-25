
#Python readline()函数
#打印1行
f = open("my_file.txt",encoding='utf-8')
# 读取一行数据
byt = f.readline()
print(byt)


#以二进制形式打开指定文件
f = open("my_file.txt",'rb')
byt = f.readline(6)
print(byt)


#Python readlines()函数
f = open("my_file.txt",'r',encoding='utf-8')
byt = f.readlines()
print(byt)


