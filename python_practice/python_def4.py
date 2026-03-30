#不定长参数
def calc_data(*args):
    min_data=min(args)
    max_data=max(args)
    avg_data=sum(args)/len(args)
    return min_data,max_data,round(avg_data,2)  

#调用函数
print(calc_data(4,3,6,7,45,33,22,44,32,89,91))
print(calc_data(4,3,6,7,45,33,22,44,32,89,31,1111,21,2233,34))


#函数 - 不定长参数（关键字参数**kwargs-->字典）
#需求：根据传入的这批数据，计算这批数据的最小值，最大值，平均值
def calc_data(*args,**kwargs):
    min_calc_data=min(args)
    max_calc_data=max(args)
    avg_calc_data=sum(args)/len(args)
    return min_calc_data,max_calc_data,round(avg_calc_data,1)

#调用函数
print(calc_data(4,3,6,7,45,33,22,44,grade=32,num=89,count=91))


#------------------------------------------>

def add (x,y):
    x+y
    return x+y
def sub(x,y):
    return x-y
def clac(x,y,oper):
    return oper(x,y)
result  = clac(4,5,sub)
print(result)


#------------------------------------------------->
#匿名函数
out_line = lambda : print("hello world")
out_line()


#计算两个数之和
add = lambda x,y:x+y
print(add(4,5))


#需求3：完成下列表的排序操作，按照一个元素的字符个数，从小到大排序：
data_list = ["hello", "world", "python", "java", "c", "c++", "c#"]
print(data_list)

data_list.sort(key=lambda item:len(item)) #匿名函数典型的应用场景
print(data_list)
data_list.sort(key=lambda item:len(item),reverse=True)
print(data_list)


#----------------------------------------------------------------------------



























