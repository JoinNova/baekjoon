#boj15651 N과M(3)
from itertools import*;n,m=map(int,input()[::2])
for _ in product([*range(1,n+1)],repeat=m):print(*_)

#by sait2000
#m,n=map(int,input().split());from itertools import*;*starmap(print,product(*[range(1,m+1)]*n)),

#by jhmoon2000
N,M=map(int,input().split())
for i in range(N**M):print(*(i//(N**j)%N+1for j in range(M-1,-1,-1)))
