'''
#如果打开文件模式中包含 w（写入），那么向文件中写入内容时，会先清空原文件中的内容，然后再写入新的内容。
f = open("a.txt", 'w',encoding='utf-8')
f.write("写入一行新数据")
f.close()

# 而如果打开文件模式中包含 a（追加），则不会清空原有内容，而是将新写入的内容会添加到原内容后边。例如，还原 a.txt 文件中的内容，并修改上面代码为：
f = open("a.txt", 'a',encoding='utf-8')
f.write("\n写入一行新数据")
f.close()

#另外，在写入文件完成后，一定要调用 close() 函数将打开的文件关闭，否则写入的内容不会保存到文件中。

#除此之外，如果向文件写入数据后，不想马上关闭文件，也可以调用文件对象提供的 flush() 函数，它可以实现将缓冲区的数据写入文件中。例如：
f = open("a.txt", 'w',encoding='utf-8')
f.write("写入一行新数据")
f.flush()

#但对于以文本格式打开的文件，必须使用缓冲区，否则 Python 解释器会 ValueError 错误。例如：
# f = open("a.txt", 'w',buffering = 0)
# f.write("写入一行新数据")
'''

'''Python writelines()函数'''
f = open('a.txt', 'r',encoding='utf-8')
n = open('b.txt','w+',encoding='utf-8')
n.writelines(f.readlines())
n.close()
f.close()

#需要注意的是，使用 writelines() 函数向文件中写入多行数据时，不会自动给各行添加换行符。
# 上面例子中，之所以 b.txt 文件中会逐行显示数据，是因为 readlines() 函数在读取各行数据时，读入了行尾的换行符。




