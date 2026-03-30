#函数定义
#计算阶乘
def factorial(n):
    """"计算阶乘的递归函数"""
    if n == 0 or n == 1 :
        return 1
    else:
        return n * factorial(n-1)

 #生成斐波那契数列
def fibonacci(n):
    """"生成斐波那契数列"""
    fib_series =[0 , 1]
    for i in range(2,n):
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

#使用函数
print(f"5的阶乘：{factorial(5)}")
print(f"斐波那契数列前10项：{fibonacci(10)}")