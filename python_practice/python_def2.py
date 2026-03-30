#函数的案例

#定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底*高/2）

def triangle_area(b,h):
    """
    根据传入的底和高计算三角形面积的函数
    :param b: 底
    :param h: 高
    :return: 三角形的面积
    """
    return b*h/2
area =triangle_area(45,60)
print("三角形的面积为：",area)


#定义一个函数：计算传入的字符串中元音字母的个数（元音字母为：aeiouAEIOU）
def count_vowel(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count+=1
    return count
vowel= count_vowel("moyitao2026nianyilufafafa")
print("元音字母的个数是：",vowel)



#定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分（保留1位小数）并返回

def class_score(s):
    max_score = max(s)
    min_score =min(s)
    avg_score = round(sum(s)/len(s),1)
    return max_score,min_score,avg_score
max_grade,min_grade,avg_grade = class_score([377,665,555,477,421,520])
print(f"最高分是：{max_grade}")
print(f"最低分是：{min_grade}")
print(f"平均分是：{avg_grade}")