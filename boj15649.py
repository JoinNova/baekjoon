#boj15649 N과M
from itertools import*;n,m=map(int,input()[::2])
for _ in permutations([*range(1,n+1)],m):print(*_)

#by sait2000
m,n=map(int,input().split());from itertools import*;*starmap(print,permutations(range(1,m+1),n)),
