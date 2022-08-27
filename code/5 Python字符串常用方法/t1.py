#
# 反转字符串
# 	源字符串
# 		"社会我顺哥, 人狠话不多"
# 	反转后
# 		"多不话狠人 ,哥顺我会社"


notice = "社会我顺哥, 人狠话不多"

# 拆字
result = ""
result2 = ""
for c in notice:
    print(c)
    # result += c # result = result + c
    result = c + result
    result2 = result2 + c
    # print(c)
print(result)
print(result2)