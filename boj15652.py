#boj15652 N과M(4)
from itertools import*;n,m=map(int,input()[::2])
for _ in combinations_with_replacement([*range(1,n+1)],m):print(*_)

#by sait2000
#m,n=map(int,input().split());from itertools import*;*starmap(print,combinations_with_
