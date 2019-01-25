#13458 시험감독


import sys;s=sys.stdin.readline
n=s()
a=list(map(int,s().split()))
b,c=map(int,s().split())
r=0
for _ in a:
    _-=b
    r+=1
    if _>0:
        r+=_//c
        if _%c>0:r+=1
print(r)
#02
s=input;n=s();i=lambda:map(int,s().split());a=[*i()];b,c=i();r=int(n)
for _ in a:
 _-=b
 if _>0:r+=_//c+1if _%c>0else _//c
print(r)
