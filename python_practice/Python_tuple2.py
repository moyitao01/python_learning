#元组操作---tuple---->元组的组包和解包

#组包==定义一个元组

#组包一：

d1=(123,132,253,645,222,222,4,3,55)

#组包二：

d2 = 23,34,45,56,33,323,45

#----------------------------------------

#解包
#解包一：
(a,s,d,f,g,h,t,c,b) = d1
print(a)
print(type(a))
#解包二(* 扩展包)：
a,*p,m=d1
print(p)
print(type(p))

#------------------------------------------------------------------------------------


students =(
    ("s001","王林",85,92,78),
    ("s002","王小虎",65,72,68),
    ("s003","张三",81,92,79),
    ("s004","李广",69,75,93),
    ("s005","赵高",77,66,88),
    ("s006","小李",90,60,78),
    ("s007","小王",80,90,88),
    ("s008","小张",65,72,68),
    ("s009","小莫",95,99,91),
    ("s010","小马",89,73,66),
)

#----------------------------------------------
#方式一：
# print("学号\t\t姓名\t\t语文\t\t数学\t\t英语")
# for s in students:
#     total = s[2]+s[3]+s[4]
#     avs = total/3
#     print(f"{s[0]}\t {s[1]}\t {s[2]}\t {total}\t {avs:.1f}")

#方式二：解包
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语")
for  id,name,Chinese,nath,English in students:
    total = Chinese+nath+English
    avs = total/3
    print(f"{id}\t { name}\t {Chinese}\t {total}\t {avs:.1f}")




Chinese_score =[s[2] for s in students]
print(Chinese_score)
math_score =[s[3] for s in students]
English_score =[s[4] for s in students]


print(f"语文最低分：{min(Chinese_score)},最高分：{max(Chinese_score)},平均分：{sum(Chinese_score)/len(Chinese_score)}")
print(f"数学最低分：{min(math_score)},最高分：{max(math_score)},平均分：{sum(math_score)/len(math_score)}")
print(f"英语最低分：{min(English_score)},最高分：{max(English_score)},平均分：{sum(English_score)/len(English_score)}")

print("优秀学生名单：")
for Id,name,Chinese,math,English in students:
    p=Chinese+math+English
    a=p/3
    if a>=90:
        print(f"学号：{Id} 姓名：{name} 平均分：{a:.1f} ")