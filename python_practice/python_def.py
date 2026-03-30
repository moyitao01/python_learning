#关于函数的学习
#函数的定义
#函数定义时并不会运行
# def my_demo():
#     print("这是我的第一个函数代码！")
#     print("你好，python！")
# my_demo()  #函数调用

#函数的参数与调用
#计算圆的面积
# def my_demo1(r):
#     """
#     计算圆的面积
#     :param r: 圆的半径
#     :return: 圆的面积
#     """
#     aer=3.14*r*r
#     # chi=2*3.14*r
#     return aer
# num1=my_demo1(10)
# print(f"圆的面积和周长为：{num1}")
# #
# #计算矩形的面积
#
# def my_demo2(a,b):
#     """
#     计算矩形的面积
#     :param a: 长
#     :param b: 宽
#     :return: 矩形的面积
#     """
#     area=a*b
#     return area
# num2 = my_demo2(10,20)
# print(f"矩形的面积是：{num2}")
#
#
# #同时计算圆的面积和周长
# def my_demo3(r):
#     """
#     分别计算圆的面积和周长
#     :param r: 圆的半径
#     :return: 圆的面积，圆的周长
#     """
#     round(3.14*r*r,2),round(2*3.14*r,2)
#     return round(3.14*r*r,2),round(2*3.14*r,2)
# num3,num4 = my_demo3(9)
# print(f"圆的面积为{num3}")
# print(f"圆的周长为{num4}")

#---------------------------------------------------------------------
#函数的嵌套
def my_demoa():
    print("a------before")
    my_demob()
    print("a------after")
def my_demob():
    print("b------before")
    my_democ()
    print("b------after")
def my_democ():
    print("c------")
    
my_demoa()