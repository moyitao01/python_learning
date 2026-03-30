# 网页处理-2
# 请修改编辑器中的代码，完成以下功能：
# 从 webpage.txt 文件中提取所有 .JPG 结尾的图像文件 URL。
# 将提取出的每个 URL 写入文件 images.txt，每行一个 URL。
#
# 输出文件示例（images.txt 内容）：
# http://image.ngchina.com.cn/2018/0829/20180829012548753.JPG
# http://image.ngchina.com.cn/2018/0823/thumb_469_352_20180823121155508.JPG
f = open(r"E:\roadway\pythonRoadway\txt_road\webpage.txt","r",encoding="utf-8")
ls = f.readlines()

jpgurl = []
for line in ls:
    if "img" in line:
        url = line.split('src=')[-1]
        if "http" in url:
            jpgurl.append(url)
f = open(r"E:\roadway\pythonRoadway\txt_road\images.txt","w",encoding="utf-8")
for url in jpgurl:
    f.write(url+'\n')
f.close()