#基于数据容器的学习开发一个教务管理系统
# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1、添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2、修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3、删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4、查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5、列出所有学生：遍历所有学生信息并输出。
# 6、统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7、退出系统。

stuents_score={}
print("欢迎来到辉哥中学教务系统!!!")
menu="""
############辉哥中学教务系统###############
#           1、添加学生信息              #
#           2、修改学生信息              #
#           3、删除学生信息              #
#           4、查询学生信息              #
#           5、列出所有学生              #
#           6、统计班级成绩              #
#           7、退出系统                 #
############辉哥中学教务系统###############
"""
while True:
    print(menu)
    choice=input("请输入你的操作（1~7）：")
    match choice:
        case "1":
            stuents=input("请输入添加的学生名字：")
            if stuents in stuents_score.keys():
                print("该学生已存在！")
            else:
                chinese_score=float(input("请输入语文成绩："))
                math_score=float(input("请输入数学成绩："))
                english_score=float(input("请输入英语成绩："))
                stuents_score[stuents]={"语文":chinese_score,"数学":math_score,"英语":english_score}
                print("添加成功！")
        case "2":
            stuents=input("请输入要修改的学生名字：")
            if stuents not in stuents_score.keys():
                print("该学生不存在！")
            else:
                chinese_score=float(input("请输入修改后的语文成绩："))
                math_score = float(input("请输入修改后的数学成绩："))
                english_score = float(input("请输入修改后的英语成绩："))
                stuents_score[stuents]={"语文":chinese_score,"数学":math_score,"英语":english_score}
                print("修改成功！")
        case "3":
            stuents=input("请输入要删除的学生名字：")
            if stuents not in stuents_score.keys():
                print("该学生不存在！")
            else:
                del stuents_score[stuents]
                print("删除成功！")
        case "4":
            stuents=input("请输入要查询的学生名字：")
            if stuents not in stuents_score.keys():
                print("该学生不存在！")
            else:
                print(f"学生姓名：{stuents},语文成绩：{stuents_score[stuents]['语文']}，数学成绩：{stuents_score[stuents]['数学']}，英语成绩：{stuents_score[stuents]['英语']}")
        case "5":
            for stuents in stuents_score.keys():
                print(f"学生姓名：{stuents},语文成绩：{stuents_score[stuents]['语文']}，数学成绩：{stuents_score[stuents]['数学']}，英语成绩：{stuents_score[stuents]['英语']}")
        case "6":  # 统计班级成绩
            chinese_aev=(sum(stuents_score[stuents]["语文"] for stuents in stuents_score.keys())/len(stuents_score.keys())) # 语文平均分
            math_aev=(sum(stuents_score[stuents]["数学"] for stuents in stuents_score.keys())/len(stuents_score.keys())) # 数学平均分
            english_aev=(sum(stuents_score[stuents]["英语"] for stuents in stuents_score.keys())/len(stuents_score.keys())) # 英语平均分
            print(f"语文平均分：{chinese_aev},数学平均分：{math_aev},英语平均分：{english_aev}")
            #统计每科成绩的最高分和最低分的学生名字：
            chinese_max=max(stuents_score[stuents]["语文"] for stuents in stuents_score.keys())
            chinese_min=min(stuents_score[stuents]["语文"] for stuents in stuents_score.keys())
            chinese_max_stuents=[(stuents,stuents_score[stuents]["语文"]) for stuents in stuents_score.keys() if stuents_score[stuents]["语文"]==chinese_max]
            chinese_min_stuents=[(stuents,stuents_score[stuents]["语文"]) for stuents in stuents_score.keys() if stuents_score[stuents]["语文"]==chinese_min]
            print(f"语文最高分：{chinese_max},最低分：{chinese_min},最高分学生：{chinese_max_stuents},最低分学生：{chinese_min_stuents}")
            math_max=max(stuents_score[stuents]["数学"] for stuents in stuents_score.keys())
            math_min=min(stuents_score[stuents]["数学"] for stuents in stuents_score.keys())
            math_max_stuents=[(stuents,stuents_score[stuents]["数学"]) for stuents in stuents_score.keys() if stuents_score[stuents]["数学"]==math_max]

            # math_max=max(stuents_score[stuents]["数学"] for stuents in stuents_score.keys())
            # math_min=min(stuents_score[stuents]["数学"] for stuents in stuents_score.keys())
            # math_max_stuents=[(stuents,stuents_score[stuents]["数学"]) for stuents in stuents_score.keys() if stuents_score[stuents]["数学"]==math_max]
            math_min_stuents=[(stuents,stuents_score[stuents]["数学"]) for stuents in stuents_score.keys() if stuents_score[stuents]["数学"]==math_min]
            print(f"数学最高分：{math_max},最低分：{math_min},最高分学生：{math_max_stuents},最低分学生：{math_min_stuents}")
            english_max=max(stuents_score[stuents]["英语"] for stuents in stuents_score.keys())
            english_min=min(stuents_score[stuents]["英语"] for stuents in stuents_score.keys())
            english_max_stuents=[(stuents,stuents_score[stuents]["英语"]) for stuents in stuents_score.keys() if stuents_score[stuents]["英语"]==english_max]
            english_min_stuents=[(stuents,stuents_score[stuents]["英语"]) for stuents in stuents_score.keys() if stuents_score[stuents]["英语"]==english_min]
            print(f"英语最高分：{english_max},最低分：{english_min},最高分学生：{english_max_stuents},最低分学生：{english_min_stuents}")
        case "7":
            print("感谢使用！！！")
            break
        case _:
            print("输入错误！！！请重新输入")
            continue

