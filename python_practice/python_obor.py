

#学生类
class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    #"姓名：张三 | 语文：90 | 数学：80 | 英语：90"
    def __str__(self):
        return f"姓名：{self.name} | 语文：| {self.chinese} | 数学：{self.math} | 英语：{self.english} | 总分：{self.chinese + self.math + self.english}"

    #修改学生的成绩
    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english


#测试
if __name__ == "__main__":
    s1 = Student("张三",90,80,90)
    print(s1)
    s1.update_score(english=88)
    print(s1)