# 循环控制

#1到10的累加

total = 0
for i in range(1,11):
    total += i
print(f"1到10的和:{total}")

#1到100 的累加

# abc = 0
# for i in range(1,101):
#     abc += i
# print(f"1到100的和：{abc}")

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}X{i}={i*j},end=\t")
    print()