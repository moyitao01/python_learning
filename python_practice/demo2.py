# 条件判断练习
# #成绩评级
# score = 85
#
# if score>= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >=70:
#     grade = "C"
# elif score >=60:
#     grade ="D"
# else:
#     grade = "F"
#
# print(f"分数:{score},等级:{grade}")
#

score = 89

if score>=90:
    grade ="优秀！"
elif score>=80:
    grade="良好！"
elif score>=60:
    grade="合格"
else:
    grade="不及格"

print(f"分数：{score},等级：{grade}")