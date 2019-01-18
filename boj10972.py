#10972 다음순열
n=int(input());k=list(range(n,0,-1))
l=list(map(int, input().split()))
if k==l:print(-1)
else:
 a=b=c=n-1
 while l[a-1]>=l[a]:a-=1
 while l[a-1]>=l[b]:b-=1
 l[a-1],l[b]=l[b],l[a-1]
 while a<c:l[a],l[c]=l[c],l[a];a+=1;c-=1
 print(*l)
