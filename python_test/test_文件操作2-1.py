result = ''
score = 0

with open(r'E:\roadway\pythonRoadway\txt_road\studs.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    for line in lines:
        students_data = int(line.split(':')[1])
        if students_data > score:
            score = students_data
            result = line
print(result)
