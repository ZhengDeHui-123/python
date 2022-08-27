
#split() 方法可以实现将一个字符串按照指定的分隔符切分成多个子串，这些子串会被保存到列表中（不包含分隔符），
# 作为方法的返回值反馈回来。该方法的基本语法格式如下：
#str.split(sep,maxsplit)


# 例如，定义一个保存 C语言中文网网址的字符串，然后用 split() 方法根据不同的分隔符进行分隔，执行过程如下：
str = "C语言中文网 >>> c.biancheng.net"
print(str)

list1 = str.split() #采用默认分隔符进行分割
print(list1)

list2 = str.split('>>>') #采用多个字符进行分割
print(list2)

list3 = str.split('.') #采用 . 号进行分割
print(list3)

list4 = str.split(' ',4) #采用空格进行分割，并规定最多只能分割成 4 个子串
print(list4)

list5 = str.split('>') #采用 > 字符进行分割
print(list5)


#需要注意的是，在未指定 sep 参数时，split() 方法默认采用空字符进行分割，
# 但当字符串中有连续的空格或其他空字符时，都会被视为一个分隔符对字符串进行分割，例如：

str = "C语言中文网   >>>   c.biancheng.net"  #包含 3 个连续的空格
list6 = str.split()
print(list6)






