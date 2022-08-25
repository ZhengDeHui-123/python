#当前程序文件同目录下没有 a.txt 文件
file = open("a.txt")
print(file)

file = open("a.txt",encoding="utf-8")
print(file)

# 以默认方式打开文件
f = open('my_file.txt')
# 输出文件是否已经关闭
print(f.closed)
# 输出访问模式
print(f.mode)
#输出编码格式
print(f.encoding)
# 输出文件名
print(f.name)
#关闭文件
f.close()
print(f.closed)

#注意，使用 open() 函数打开的文件对象，必须手动进行关闭（后续章节会详细讲解），Python 垃圾回收机制无法自动回收打开文件所占用的资源。

#with 语句可以保证系统自动关闭打开的文件
#with open (filename,mode) as f: