# 请修改编辑器中的代码，完成以下功能：获取用户输入的一个整数，记为 n，以 100 为随机数种子，随机生成10个1到 n 之间的随机数，并输出生成的随机数，数字之间以逗号分隔。
#
# 输入示例：
# 900
#
# 输出示例：
# 150,471,466,790,777,723,403,750,359,444

import random
n = int(input("请输入正整数:"))
random.seed(100)
for i in range(10):
    if i < 10:
       print(random.randint(1,n),end=",")
    else:
        print(random.randint(1,n))
