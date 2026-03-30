#传参
#定义函数
def reg_stu(name,age,gender,city):
    print(f"姓名：{name} 年龄：{age} 性别：{gender} 城市：{city}")
    return{"name":name,"age":age,"gender":gender,"city":city}


#传参方式一：位置传参
stu = reg_stu("张三",18,"男","上海")
print(stu)

#传参方式二：关键字参数

stu = reg_stu(name="小莫",age=18,gender="男",city="贵州")
print(stu)
#传参方式三：混合参数
stu = reg_stu("小王",22,gender="女",city="四川")
print(stu)