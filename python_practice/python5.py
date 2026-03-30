#5、字典练习
#学生信息管理系统
student = {
    "name": "张三",
    "age": "20",
    "coursers":["数学","英语","物理"],
    "scores":{"数学":90,"英语":85,"物理":88}
}

#访问和修改
print(f"学生姓名：{student['name']}")
student["age"] = 21
student["scores"]["数学"] = 92

#遍历字典
print("\n所有课程成绩：")
for course,score in student["scores"].items():
    print(f"{course}:{score}分")

    #计算平均分
    average = sum(student["scores"].values()) / len(student["scores"])
    print(f"平均分：{average:.2f}")