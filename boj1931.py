#boj1931회의소배정
n=int(input());l=sorted([*map(int,input().split()[::-1])]for _ in'_'*n);f=0;r=0
for _ in l:
 if _[1]>=f:r+=1;f=_[0]
print(r)
