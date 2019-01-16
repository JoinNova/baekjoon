#1021 회전하는큐

from sys import stdin
n,m=map(int,stdin.readline().split())
l=list(range(1,n+1))
p=list(map(int,stdin.readline().split()))
result=0
for _ in p:
    mv=0    
    while True:
        if _==l[0]:            
            if mv<=len(l)-mv:
                result+=mv
            else:
                result+=len(l)-mv
            del(l[0])
            break
        top=l[len(l)-1]
        l.pop()
        l.insert(0,top)
        mv+=1
print(result)

#02
n,m=map(int,input().split());l=list(range(1,n+1));p=list(map(int,input().split()));r=0
for _ in p:
 v=0
 while 1:
  if _==l[0]:
   r+=v if v*2<=len(l) else len(l)-v;del(l[0]);break
  t=l[-1];l.pop();l.insert(0,t);v+=1
print(r)
