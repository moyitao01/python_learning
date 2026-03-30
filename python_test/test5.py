#阿来伯数字替换为汉字数字
n = input()
s = "〇一二三四五六七八九"
for c in "0123456789":
     n=n.replace(c,s[int(c):int(c)+1])
print(n)