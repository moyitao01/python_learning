#元组基本操作 ---tuple--->元素可重复出现，有序，元素不可修改
#定义
t1 = (1,2,3,4,5,6,7,8,9,10,44,11,2,4)
print(t1)
print(type(t1))
#索引
print(t1[0])
print(t1[-1])

#切片
print(t1[0:5])
print(t1[::-1])
print(t1[0::2])

#统计元素的个数
print(t1.count(2))

#查看索引位置
print(t1.index(44))


#空元组
t2=()
print(t2)
print(type(t2))

#单个元素的元组操作
#正确操作
t3=(122,)
print(type(t3))

#错误操作
t4=(123)
print(type(t4))
