# 请修改编辑器中的代码，完成以下功能：
# 读取 studs.txt 文件中的学生姓名和分数。
# 找出分数最高的学生，并将其姓名和分数输出在屏幕上，格式为“姓名:分数”。
#
# 输出示例：
# 李四:450

result = ''
score = 0
with open(r'E:\roadway\pythonRoadway\txt_road\data.txt','r',encoding='utf-8') as file:

    for line in file.readlines():
        score_data = int(line.split(':')[1])

        if score_data >score:
             score = score_data
             result = line
print(result)
