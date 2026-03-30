# 考生文件夹下的 data.txt.txt 文件包含学生的姓名、班级和分数信息
#
# 请修改编辑器中的代码，完成以下功能：
# 读取 data.txt.txt 文件，将每位学生的姓名和分数提取出来。
# 将提取出的信息写入文件 studs.txt，每行记录格式为“姓名:分数”，用英文冒号隔开。
# 输出文件示例（studs.txt 内容）：
# 王一:340
# 李四:150


# with open(r'/txt_road/data.txt', 'r', encoding='utf-8') as file:
#     lines = file.readlines()
#     #提取学生的姓名和分数
#     students_scores = []
#     for line in lines:
#         name,rest = line.split(':')
#         _,score = rest.split(',')
#         #添加到列表中
#         students_scores.append(f"{name}:{score.strip()}")
#
#         #将提取的信息写入studs.txt文件
#         with open(r'E:\roadway\pythonRoadway\txt_road\studs.txt','w',encoding='utf-8') as output_file:
#             for student in students_scores:
#                 output_file.write(student + '\n')
# with open(r'E:\roadway\pythonRoadway\txt_road\data.txt','r',encoding='utf-8') as f:
#     lines =f.readlines()
#
# with open(r'E:\roadway\pythonRoadway\txt_road\test.txt','w',encoding='utf-8') as open_file:
#      open_file.writelines(lines)
# with open(r'E:\mo.txt','w',encoding='utf-8') as wr:
#     for i in range(1,101):
#         wr.write("小莫最牛逼！小莫最牛逼！小莫最牛逼！小莫最牛逼！小莫最牛逼！\n")
#         wr.write("今年发发发！\n")
#         wr.write("小莫是AI开发大师！python编程高手！人生赢家！\n")
# with open(r'E:\roadway\pythonRoadway\txt_road\data.txt','r',encoding='utf-8') as ui:
#     lines = ui.readlines()
# with open(r'E:\roadway\pythonRoadway\txt_road\xi.txt','w',encoding='utf-8') as ho:
#     ho.writelines(lines)



# 考生文件夹下的 data.txt 文件包含学生的姓名、班级和分数信息
# 请修改编辑器中的代码，完成以下功能：
# 读取 data.txt.txt 文件，将每位学生的姓名和分数提取出来。
# 将提取出的信息写入文件 studs.txt，每行记录格式为“姓名:分数”，用英文冒号隔开。
# 输出文件示例（studs.txt 内容）：
# 王一:340
# 李四:150


with open(r'E:\roadway\pythonRoadway\txt_road\data.txt','r',encoding='utf-8') as file:
    lines = file.readlines()
    
    students_scores = []

    for line in lines:
        name,rest =line.split(':')
        _,score = rest.split(',')
        students_scores.append(f"{name}:{score.strip()}")
        with open(r'E:\roadway\pythonRoadway\txt_road\studs.txt','w',encoding='utf-8') as output_file:
            for student in students_scores:
                output_file.write(student + '\n')



























