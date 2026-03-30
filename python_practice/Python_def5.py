#函数的递归调用
#利用函数计算n的阶乘
def jc(n):
    """
    :param n: 输入一个数
    :return: 返回阶乘
    """
    if n==1:
        return 1
    else:
        return n*jc(n-1)
print(jc(1))
