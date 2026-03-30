# # a= 100  b=200  c =300 c,a,b
#
# a= 100
# b= 200
# c= 300
#
# a,b,c = c,a,b
#
# num=10
# s = "小莫说："
# s1 = "如果想"
# s2 = 888
# s3="必须好好学技术！！！"
#
# name = input("请输入你的名字：")
# print(f"{name}")
# age = input("请输入你的年龄：")
# print(f"{age}")
# print(num)
# print(type(num))
# print(type("hello"))
# print(isinstance(num,int))
# print(isinstance("hello",int))
# print(s + s1 + str(s2) + s3)
# print("小莫说：如果想%s必须好好学技术！！！"%s2)
# print(f"小莫说：如果想{s2}必须好好学技术！！！")
# demo = 1000
# num = input("请输入密码：")
# num2 = input("请输入取出的金额：")
# less = demo - int(num2)
# print(f"密码正确！")
# print(f"已成功取出{num2}！")
# print(f"剩余金额为{less}")
# x = int(input("请输入x的值："))
# y = int(input("请输入y的值："))
# print(f"x+y={x+y},"+f"x-y={x - y}")

# uu = int(input("请输入账号："))
# pp = int(input("请输入密码："))
#
# if uu ==234556 and pp == 123456 :
#     print("登录成功！")
# else:
#     print("登录失败！")
# a = int(input("请输入一个数字："))
#
# if a//2 ==0:
#     print(f"{a}为偶数！")
#
# else:
#     print(f"{a}为奇数！")
#
# if a>=18:
#     print("已成年")
# else:
#     print("未成年")
# if a>0:
#     print("正数")
# elif a<0:
#     print("负数")
# else:
#     print("零")
#
# if a>=60:
#     print("及格")
# else:
#     print("不及格")

# for i in range(1,101):
#     if i%2==0:
#         print(i)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}X{j}={i*j},end=\t")
#     print()
# day = str(input("请输入星期几："))
#
# match day:
#     case "星期一":
#         print("今天早八！")
#     case "星期二":
#         print("今天python课！")
#     case "星期三":
#         print("今天Spring Boot课！")
#     case "星期四":
#         print("今天是软件工程课！")
#
#     case "星期五":
#         print("今天要放学了！！！")
#     case "星期六"|"星期日":
#         print("今天不上课！")
#     case _:
#         print("输入错误！！！")
i=0
# while i<10:
#     print("小莫2026年暴富！！！")
#     i+=1
# else:
#     print("循环结束")

# total=0
# while i<=100:
#     i+=1
#     if i%2==0:
#         total+=i
#         print(total)
# total=0
# for i in range(1,101):
#     if i%2!=0:
#         total+=i
# print(total)
#
#
# num=0
# for i in range(100,501):
#     if i%3==0:
#         num+=i
#         print(num)
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}X{i}={i*j}",end="\t")
#     print()
# 外层循环控制行数（1到9）
# for i in range(1, 10):
#     # 内层循环控制每行的列数（1到当前行数i）
#     for j in range(1, i + 1):
#         # 格式化输出乘法表达式，保证对齐（每个表达式占8个字符宽度）
#         print(f"{j} × {i} = {i*j}", end="\t")
#     # 每行结束后换行
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}X{i}={i*j}",end="\t")
#     print()
#


#
# for i in range(1,7):
#     for j in range(1,i+1):
#         print(f"{j}",end="\t")
#     print()


#国际象棋棋盘生成
# for i in range(1,9):
#     for j in range(8):
#         if (i+j)%2==0:
#             print("■",end="\t")
#         else:
#             print("□",end="\t")
#     print()
#

#循环代码和If生成简易的用户密码登录
# while True:
#     username=input("请输入用户名：")
#     password=input("请输入密码：")
#     if username=="" or password=="":
#         print("用户名和密码不能为空！请重新输入：")
#         continue
#     if username=="admin" and password=="123456":
#         print("登录成功！")
#         break
#     elif username=="abc" and password=="222333":
#         print("登录成功！！")
#         break
#     elif username=="cad" and password=="33338888":
#         print("登录成功！！")
#         break
#     else:
#         print("输入的用户名和密码不正确！请请重新输入：")

#代码随机生成一个数，输入数字猜猜对不对
# import random
#
# random_num=random.randint(1,100)
#
# while True:
#     num = int(input("请输入数字："))
#
#     if num>random_num:
#         print("太大了！")
#     elif num<random_num:
#         print("太小了！")
#     else:
#         print("恭喜你猜对了！")
#         break
# print(random_num)

#列表

# s=[23,34,34,88,"dji",90,122,]
# print(s)
# print(s[0])
# print(s[-3])
# s[4]="makabaka"
# del s[3]
#
# print(s)


#列表的常用方法

# s=[23,34,34,88,"dji",90,122,]
#
# s.append(100)
# print(s)
# s.insert(1,33)
# print(s)
# s.pop(5)
# print(s)
# s.sort()
# print(s)
# s.remove(34)
# print(s)
# s.reverse()
# print(s)

#列表案例

# num_list=[]
#
# for i in range(10):
#     num=int(input("请输入数字："))
#     num_list.append(num)
#
#     num_list.sort()
# print(num_list)
#
# print("最小值：",min(num_list))
# print("最大值：",max(num_list))
# print("平均值：",sum(num_list)/len(num_list))

# 列表合并和去重

# num_list1=[12,34,56,78,90,12,34,56,78,90]
# num_list2=[12,23,34,45,56,67,78,89,90,11]

#利用for循环将num_list2中的元素导入num_list1中
# for num in num_list2:
#     num_list1.append(num)
# print("合并后的列表为：",num_list1)
#
#
# num_list=[]
# for num in num_list1:
#     if num not in num_list:
#         num_list.append(num)
# print("去重之后的列表：",num_list)


# num_list=[12,34,56,78,90,12,34,56,78,90]
# # num_list1= []
# # for num in num_list:
# #     if num%2==0:
# #         num_list1.append(num**2)
# #
# # print(num_list1)
# num_list1=[num**2 for num in num_list if num%2==0]
# print(num_list1)


#字符串操作常用方法：
# s = "Python-Hello-word"
#
# ss = s.find("-")
# print(ss)
#
# sr = s.count("-")
# print( sr)
#
# sa = s.upper()
# print(sa)
#
# st = s.lower()
# print(st)
#
# sv = s.split(" ")
# print(sv)
#
# se =s.replace("Python","Makabaka")
# print(se)
#
# sb = s.startswith("Python")
# print(sb)

#字符串案例
# road = input("请输入你想输入的：")
#
# if road[::]==road[::-1]:
#     print("是回文！")
# else:
#     print("不是回文！")


# scr = input("请输入一个字符串：")
# print(scr)
# ddc = scr[::-1]
# print(ddc)
#
# ccd = ddc.split(" ")
# print(ccd)

# 初始化空列表
# result_list = []
#
# # 循环输入10个字符串
# for i in range(10):
#     s = input(f"请输入第{i+1}个字符串：")
#     # 反转字符串并转大写
#     processed = s[::-1].upper()
#     result_list.append(processed)
#
# # 遍历输出列表内容
# print("\n处理后的列表内容：")
# for item in result_list:
#     print(item)

num_list=[]
for i in range(10):
    num=input(f"你的第{i+1}个字符串；")
    s=num[::-1].upper()
    num_list.append(s)


print ("\n遍历输出的结果：")
for j in num_list:
    print(j)