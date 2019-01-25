#2167 2차원배열의 합 pypy3

import sys;s=sys.stdin.readline
l=[];n,m=map(int,s().split())
l+=[[*map(int,s().split())]for i in'a'*n]
for a in'a'*int(s()):
    i,j,x,y=map(int,s().split());r=0;j-=1
    for _ in range(i-1,x):
        k=l[_]
        r+=sum(k[j:y])
    print(r)

#02 python3 속도높이기
import sys;s=sys.stdin.readline
l=[];n,m=map(int,s().split())
for i in'a'*n:
    h=0;u=[]
    for _ in input().split():
        h+=int(_)
        u+=[h]
    l+=[u]
#print(l)
for a in'a'*int(s()):
    i,j,x,y=map(int,s().split());r=0
    for _ in range(i-1,x):
        k=l[_]
        if j==1:
            #print(r,k,k[y-1],k[j-1])
            r+=k[y-1]
        else:
            #print(r,k,k[y-1],k[j-1])
            r+=k[y-1]-k[j-2]
    print(r)

#03 short
s=input;l=[];n,m=map(int,s().split())
for i in'a'*n:
 h=0;u=[]
 for _ in s().split():h+=int(_);u+=[h]
 l+=[u]
for a in'a'*int(s()):
 i,j,x,y=map(int,s().split());r=0
 for _ in range(i-1,x):k=l[_];r+=k[y-1]if j<2 else k[y-1]-k[j-2]
 print(r)
