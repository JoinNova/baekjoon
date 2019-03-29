#boj16650 Counting Stairs
import sys;s=sys.stdin;mod=998244353;size=200000
way=[0 for _ in'_'*(size+1)]
stair=[0 for _ in'_'*(size+1)]
stair[0]=1;i=1
while 1:
    if i**2>size:break
    j=0
    while 1:
        if j>size:break
        if j>=i:
            stair[j]+=stair[j-i]
            stair[j]%=mod
        idx=j*2+i**2
        if idx<=size:
            way[idx]+=stair[j]
            way[idx]%=mod
        j+=1
    i+=1

int(s.readline())
for _ in s:print(way[int(_)])
