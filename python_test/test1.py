# def f(n):
#     s=0
#     if n%2!=0:
#         for i in range(1,n+1,2):
#             s+=1/i
#     else:
#         for i in range(2,n+1,2):
#             s+=1/i
#         return s
# n=int(input())
# print(f(n))

def f(n):
  s=0
  if n%2:
      for i in range(1,n+1,2):
          s+=1/i
  else:
      for i in range(2,n+1,2):
          s+=1/i
  return s
n = int(input())
print(round(f(n),2))#保留两位小数