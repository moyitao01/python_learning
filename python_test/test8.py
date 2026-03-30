# 请修改编辑器中的代码，完成以下功能：键盘输入一段文本，保存在字符串变量 s 中，分别使用 Python 内置函数及 jieba 库中的函数计算字符串 s 的中文字符个数及中文词语个数。注意：中文字符包括中文标点符号。
#
# 输入示例：
# 俄罗斯举办世界杯
#
# 输出示例：
# 中文字符数为8，中文词语数为3。
# import pkg_resources
# import jieba
# s = input("请输入一个字符串:")
# n = len(s)
# m = len(jieba.lcut(s))
# print("中文字符数为{}，中文词语数为{}。".format(n, m))

import jieba
s = input("请输入一个字符串:")
n = len(s)
m = len(jieba.lcut(s))
print("中文字符数为{}，中文词语数为{}。".format(n, m))
