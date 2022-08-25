

#http://c.biancheng.net/view/4645.html

# 导入模块方式一：临时添加模块完整路径
# import sys
# sys.path.append('D:\\python_module')

# 导入模块方式二：将模块保存到指定位置

import sys
for i in sys.path:
    print(i)

#导入模块方式三：设置环境变量
#Windows 环境变量，变量名 PYTHONPATH 变量值：.;d:\python_ module
