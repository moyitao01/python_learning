#字典
#定义字典
# dict ={"小莫":788,"王永永":677,"马竞":658}
# print(dict)
# print(type(dict))
# print(dict["小莫"])
# dict["马竞"] = 666
# print(dict)


#---------------------------------------------------

#字典的基本操作
# dict1 = {"涛哥":788,"永哥":549,"马哥":533,"浩哥":666,"权哥":433,"雄哥":344,"安哥":222}
# print(dict1)
# #添加
# dict1["威哥"]=444
# print(dict1)
#
# #删除
# del dict1["马哥"]
# print(dict1)
#
# #修改
# dict1["雄哥"]=500
# print(dict1)
#
# #查询
# print(dict1.get("涛哥"))
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
#
# #遍历
# for key,value in dict1.items():
#     print(key,value)

#---------------------------------------------------------
#案例----------------思想是 a={{b:c},{g:h}----}
# 购物车管理系统
shopping_cart= {}
print("欢迎使用商品管理系统！！！")
num="""
##############商品管理系统##############
#             1、添加商品             #
#             2、修改商品             #
#             3、删除商品             #
#             4、查询商品             #
#             5、退出系统             #
#####################################
"""

while True:
    print(num)  # 打印菜单
    choice=input("请输入你操作（1~5）:")
    match choice: # 匹配
     case "1":
         goods_name=input("请输入商品名称：")
         if goods_name in shopping_cart: # 判断商品是否存在
             print("商品已存在！")
         else:
          goods_price=float(input("请输入商品价格："))
          goods_num=int(input("请输入商品数量："))
          shopping_cart[goods_name]={"price":goods_price,"num":goods_num} # 添加商品
          print("已成功添加商品！")

     case "2":
        goods_name = input("请输入要修改的商品名称：")
        if goods_name not in shopping_cart:
            print("商品不存在！")
        else:
         goods_price = float(input("请输入最新的商品价格："))
         goods_num = int(input("请输入最新的商品数量："))
         shopping_cart[goods_name]={"price":goods_price,"num":goods_num}
         print("已修改商品信息！")
     case "3":
         goods_name = input("请输入要删除的商品名称：")
         if goods_name not in shopping_cart:
             print("商品不存在！")
         else:
             del shopping_cart[goods_name]
             print("已删除商品！")

     case "4":
         for goods_name in shopping_cart.keys():
             goods_info = shopping_cart[goods_name]
             print(f"商品名称:{goods_name},商品价格：{goods_info['price']},商品数量：{goods_info['num']}")
     case "5":
         print("再见！")
         break
     case _:
        print("输入错误！！！请重新输入")
