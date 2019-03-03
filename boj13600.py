#boj13600 Factorial
from math import factorial as f
n=int(input());result=0
for i in range(int(n**.5),0,-1):
    while 1:
        if f(i)<=n:
            result+=1
            n-=f(i)
        else:break
    if n<=0:break
print(result)
