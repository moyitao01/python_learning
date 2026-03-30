with open(r'E:\roadway\pythonRoadway\txt_road\webpage.txt', 'r', encoding='utf-8') as f:
    ls = f.readlines()

num = 0
for line in ls:
    if "img" in line:
        url = line.split('src=')[-1].split('"')
        if "http" in url:
            num = num + 1

print(num)