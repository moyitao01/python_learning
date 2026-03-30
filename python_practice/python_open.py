# #文件的读写操作
# #打开文件
# # f = open("E:/test.txt","r",encoding="utf-8")
# # # print(f.read()) #读取文件
# # # print(f.readlines()) #读取文件，以列表的形式返回
# # print(f.readline(8))  #读取指定行数
#
#
# # ... existing code ...
# # 读取并写入文件的Python代码
# def read_and_write_file():
#     file_path = "E:\\test.txt"
#
#     # 先读取文件内容
#     with open(file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         print("原文件内容：")
#         print(content)
#
#     # 修改写入模式为追加模式'a'，并在内容前后添加换行符以保持格式整洁
#     with open(file_path, 'a', encoding='utf-8') as file:
#         file.write("\n我已经打开了你的文件，哈哈哈！")
#
#     print("已成功在文件末尾添加新内容！")
#
# # ... existing code ...
