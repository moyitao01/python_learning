#裴波那契数列

a, b = 0, 1
while a<=100:
    print(a, end=',')
    a, b = b,b+a
