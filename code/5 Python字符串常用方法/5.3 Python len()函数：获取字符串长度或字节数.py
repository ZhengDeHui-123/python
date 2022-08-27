
#汉字在 GBK/GB2312 编码中占用 2 个字节，而在 UTF-8 编码中一般占用 3 个字节。

a='http://c.biancheng.net'
print(len(a))

#因为汉字加中文标点符号共 7 个，占 21 个字节，而英文字母和英文的标点符号占 6 个字节，一共占用 27 个字节。
str1 = "人生苦短，我用Python"
print(len(str1.encode()))

str2 = "人生苦短，我用Python"
print(len(str2.encode('gbk')))