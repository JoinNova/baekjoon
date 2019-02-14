#boj14659 한조서열정리하고옴ㅋㅋ
n=int(input())
l=[*map(int,input().split())];
#l=list(range(30001,0,-1))
s=l[0];m=c=0
for _ in l[1:]:
    if _<s:
        c+=1
    else:
        s=_;c=0
    m=max(m,c)
print(m)

#02
input();l=[*map(int,input().split())];s=l[0];m=c=0
for _ in l[1:]:
 if _<s:c+=1
 else:s=_;c=0
 m=max(m,c)
print(m)
