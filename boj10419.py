#boj10419 지각
n=int(input())
for i in range(n):
    t=int(input())
    for j in range(t+1):
        if j+j**2>t:print(j-1 if j+j**2>t else j);break
