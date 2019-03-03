#boj10986 나머지합
import sys;s=sys.stdin.readline
n,m=map(int, s().split())
l=[0]+[a%m for a in map(int,s().split())];ll=[0]
result=0;namerge=[0]*m
for i in range(n):
    ll.append((ll[i]+l[i+1])%m)
for i in range(n+1):
    namerge[ll[i]]+=1
for i in range(m):
    if namerge[i]<2:pass
    result+=namerge[i]*(namerge[i]-1)
print(result//2)
