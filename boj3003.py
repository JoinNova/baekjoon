#boj3003 킹, 퀸, 룩, 비숍, 나이트, 폰
l=[1,1,2,2,2,8];i=0
for _ in map(int,input().split()):l[i]=l[i]-_;i+=1
print(*l)
