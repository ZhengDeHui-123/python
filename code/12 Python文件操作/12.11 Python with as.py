
'''
首先学习如何使用 with as 语句。with as 语句的基本语法格式为：
with 表达式 [as target]：
    代码块
此格式中，用 [] 括起来的部分可以使用，也可以省略。其中，target 参数用于指定一个变量，该语句会将 expression 指定的结果保存到该变量中。
with as 语句中的代码块如果不想执行任何语句，可以直接使用 pass 语句代替。
'''

# 举个例子，假设有一个 a.txt 文件，其存储内容如下：

with open('a.txt', 'a',encoding='utf-8') as f:
    f.write("\nPython教程")