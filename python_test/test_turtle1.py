import turtle

# 设置画布
screen = turtle.Screen()
screen.title("小朋友")
screen.bgcolor("skyblue")

# 创建画笔
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(2)

# 1. 画头部（圆形）
pen.penup()
pen.goto(0, 100)
pen.pendown()
pen.color("peachpuff", "peachpuff")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

# 2. 画头发
pen.penup()
pen.goto(-40, 140)
pen.pendown()
pen.color("black", "black")
pen.begin_fill()
pen.setheading(0)
for _ in range(3):
    pen.forward(26)
    pen.right(120)
pen.end_fill()

# 3. 画眼睛
# 左眼
pen.penup()
pen.goto(-15, 130)
pen.pendown()
pen.color("black", "black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# 右眼
pen.penup()
pen.goto(15, 130)
pen.pendown()
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# 4. 画嘴巴（微笑）
pen.penup()
pen.goto(-15, 115)
pen.pendown()
pen.setheading(-90)
pen.width(3)
pen.circle(15, 180)
pen.width(2)

# 5. 画身体（长方形）
pen.penup()
pen.goto(-30, 100)
pen.pendown()
pen.color("red", "red")
pen.begin_fill()
pen.setheading(-90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(60)
pen.end_fill()

# 6. 画左手臂
pen.penup()
pen.goto(-30, 90)
pen.pendown()
pen.color("peachpuff", "peachpuff")
pen.begin_fill()
pen.setheading(180)
pen.forward(30)
pen.right(90)
pen.forward(40)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.forward(40)
pen.end_fill()

# 7. 右手臂
pen.penup()
pen.goto(30, 90)
pen.pendown()
pen.begin_fill()
pen.setheading(0)
pen.forward(30)
pen.left(90)
pen.forward(40)
pen.left(90)
pen.forward(10)
pen.left(90)
pen.forward(40)
pen.end_fill()

# 8. 画左腿
pen.penup()
pen.goto(-20, 40)
pen.pendown()
pen.color("blue", "blue")
pen.begin_fill()
pen.setheading(-90)
pen.forward(50)
pen.right(90)
pen.forward(15)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(15)
pen.end_fill()

# 9. 画右腿
pen.penup()
pen.goto(5, 40)
pen.pendown()
pen.begin_fill()
pen.setheading(-90)
pen.forward(50)
pen.right(90)
pen.forward(15)
pen.right(90)
pen.forward(50)
pen.right(90)
pen.forward(15)
pen.end_fill()

# 10. 画左脚
pen.penup()
pen.goto(-20, -10)
pen.pendown()
pen.color("black", "black")
pen.begin_fill()
pen.setheading(0)
pen.forward(15)
pen.right(90)
pen.forward(10)
pen.right(90)
pen.forward(15)
pen.end_fill()

# 11. 画右脚
pen.penup()
pen.goto(5, -10)
pen.pendown()
pen.begin_fill()
pen.forward(15)
pen.left(90)
pen.forward(10)
pen.left(90)
pen.forward(15)
pen.end_fill()

# 隐藏画笔
pen.hideturtle()

# 添加文字
pen.penup()
pen.goto(-50, -50)
pen.color("darkblue")
pen.write("小朋友", font=("Arial", 16, "bold"))

# 点击关闭窗口
screen.exitonclick()
