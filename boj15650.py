#boj15649 N과M(2)
from itertools import*;n,m=map(int,input()[::2])
for _ in combinations([*range(1,n+1)],m):print(*_)

#by sait2000
m,n=map(int,input().split());from itertools import*;*starmap(print,combinations(range(
