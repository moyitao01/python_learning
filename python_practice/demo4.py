#列表创建和操作
fruits = ["苹果","香蕉","橙子","草莓"]

#遍历
for i,fruit in enumerate(fruits):
    print(f"第{i+1}种水果：{fruit}")

#列表推导式
numbers = [x**2 for x in range(1,6)]
print(f"1-5的平方：{numbers}")


#列表方法
fruits.append("葡萄")
fruits.insert(1,"芒果")
fruits.remove("香蕉")
print(f"更新后的水果列表:{fruits}")