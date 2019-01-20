#11659 구간 합 구하기4
import sys
s=sys.stdin.readline;l=[0]
n,m=map(int,s().split());d=dict();i=0
for _ in s().split():
    i+=int(_)
    l+=[i]
for _ in range(m):
    x,y=map(int,s().split())
    print(l[y]-l[x-1])
#02
import sys;i=sys.stdin.readline;l=[0];n,m=map(int,i().split());a=0
for _ in i().split():a+=int(_);l+=[a]
for _ in'a'*m:x,y=map(int,i().split());print(l[y]-l[x-1])
