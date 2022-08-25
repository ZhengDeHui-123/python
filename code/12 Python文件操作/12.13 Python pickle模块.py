
'''
pickle 模块提供了以下 4 个函数供我们使用：
dumps()：将 Python 中的对象序列化成二进制对象，并返回；
loads()：读取给定的二进制对象数据，并将其转换为 Python 对象；
dump()：将 Python 中的对象序列化成二进制对象，并写入文件；
load()：读取指定的序列化数据文件，并返回对象。

以上这 4 个函数可以分成两类，其中 dumps 和 loads 实现基于内存的 Python 对象与二进制互转；
dump 和 load 实现基于文件的 Python 对象与二进制互转。
'''

'''
pickle.dumps()函数
此函数用于将 Python 对象转为二进制对象，其语法格式如下：
dumps(obj, protocol=None, *, fix_imports=True)
'''

#【例 1】
import pickle
tup1 = ('I love Python', {1,2,3}, None)
#使用 dumps() 函数将 tup1 转成 p1
p1 = pickle.dumps(tup1)
print(p1)


'''
pickle.loads()函数
此函数用于将二进制对象转换成 Python 对象，其基本格式如下：
loads(data, *, fix_imports=True, encoding='ASCII', errors='strict')

其中，data 参数表示要转换的二进制对象，其它参数只是为了兼容 Python 2.x 版本而保留的，可以忽略。
'''

# 【例 2】在例 1 的基础上，将 p1 对象反序列化为 Python 对象。
import pickle
tup1 = ('I love Python', {1,2,3}, None)
p1 = pickle.dumps(tup1)
#使用 loads() 函数将 p1 转成 Python 对象
t2 = pickle.loads(p1)
print(t2)

'''
pickle.dump()函数
此函数用于将 Python 对象转换成二进制文件，其基本语法格式为：
dump (obj, file,protocol=None, *, fix mports=True)
'''

#【例 3】将 tup1 元组转换成二进制对象文件。import pickle
tup1 = ('I love Python', {1,2,3}, None)
#使用 dumps() 函数将 tup1 转成 p1
with open ("a.txt", 'wb') as f: #打开文件
    pickle.dump(tup1, f) #用 dump 函数将 Python 对象转成二进制对象文件



'''
pickle.load()函数
此函数和 dump() 函数相对应，用于将二进制对象文件转换成 Python 对象。该函数的基本语法格式为：
load(file, *, fix_imports=True, encoding='ASCII', errors='strict')
'''

#【例 4】将例 3 转换的 a.txt 二进制文件对象转换为 Python 对象。
import pickle
tup1 = ('I love Python', {1,2,3}, None)
#使用 dumps() 函数将 tup1 转成 p1
with open ("a.txt", 'wb') as f: #打开文件
    pickle.dump(tup1, f) #用 dump 函数将 Python 对象转成二进制对象文件
with open ("a.txt", 'rb') as f: #打开文件
    t3 = pickle.load(f) #将二进制文件对象转换成 Python 对象
    print(t3)





