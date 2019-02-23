#boj1448 삼각형의만들기
import sys;s=sys.stdin.readline
n=int(s());l=[False]*n;result=-1
for i in range(n):
    l[i]=int(s())
l.sort(reverse=True)
for i in range(n-2):
    if l[i]<l[i+1]+l[i+2]:
        result=sum([l[i],l[i+1],l[i+2]])
        break
        
print(result)
