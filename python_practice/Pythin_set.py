#集合
#集合的定义
# s = {12,24,45,676,54,34,45,44,55,66,55,44,12}
# print(s)
# print(type(s))
#
# #空集合的表示
# t = set()
# print(t)
# print(type(t))
#
# #集合的常用方法
# s1={12,34,56,78,90,12,34,56,78,90}
# print(s1)
#
# #添加元素
# s1.add(100)
# print(s1)
#
# #删除元素
# s1.remove(34)
# print(s1)
#
# e=s1.pop()
# print(e)
#
# # s1.clear()
# # print(s1)
#
# s.intersection(s1)   #求交集
# print(s.intersection(s1))   #求交集
# print(s.union(s1))   #求并集
# print(s.difference(s1))   #求差集




#------------------------------------------------------------------

#案例1：

#选修足球学生名单：
football_set = {"王永永","小莫","赵宇","王伟伟","码垛机","李瑾","何晓东","马超"}
#选修篮球学生名单：
basketball_set = {"王永永","孙金飞","赵宇","小莫","马超","江森","李文文","蒋天生","韦世豪"}
#选修羽毛球学生名单：
badminton_set = {"小莫","小明","王永永","菏泽","东京","孔明世家","电解镍","省得你"}
#选修艺术学生名单：
art_set = {"王伟伟","小王","小莫","马婧","张天昊","熊峰","李明珠","方冰冰","肖天浩","马超","小明"}


#求同时选修足球和篮球的学生名单：
#方式一：
foba_set = football_set.intersection(basketball_set)
print(foba_set)
#方式二：
foba1_set = football_set & basketball_set
print(foba1_set)

#求同时选修四门课的学生名单:
#方式一：
fobab_set = football_set.intersection(basketball_set,badminton_set,art_set)
print(fobab_set)
#方式二：
all_set = football_set & basketball_set & badminton_set & art_set
print(all_set)

#求选修篮球但是没有选修足球的学生名单：
#方式一：
foba3_set = basketball_set.difference(football_set)
print(foba3_set)

#方式二：
foba4_set =basketball_set - football_set
print(foba4_set)

#方式三：
foba5_set = {s for s in basketball_set if s not in football_set}
print(foba5_set)

#统计每个同学选修了多少门课程：

#先统计有哪些同学，利用集合的元素不可重复的性质统计：
ell_set = football_set.union(basketball_set,badminton_set,art_set)
print(ell_set)
All_set = football_set | basketball_set | badminton_set | art_set
print(All_set)

#利用列表的性质，解包集合，利用列表的count方法统计出现的词次数来统计修了几门课程
all_list =[*basketball_set,*football_set,*badminton_set,*art_set]
for s in All_set:
    print(f"{s}选修了{all_list.count(s)}门课程")