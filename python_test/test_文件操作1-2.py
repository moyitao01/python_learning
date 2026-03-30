with open(r'E:\roadway\pythonRoadway\txt_road\data.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    students_score = []
    for score in lines:
        name, rest = score.split(':')
        _, goal = rest.split(',')
        students_score.append(f"{name}:{goal.strip()}")

with open(r'E:\roadway\pythonRoadway\txt_road\studs.txt', 'w', encoding='utf-8') as scores:
    for goal in students_score:
        scores.write(goal + '\n')

print("学生姓名和成绩提取完成，已成功保存到studs.txt")