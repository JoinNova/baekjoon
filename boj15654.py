#boj15654 N&M(6)
from itertools import*;n,m=map(int,input()[::2])
for _ in permutations(sorted(map(int,input().split())),m):print(*_)

#02
m,n=map(int,input().split());from itertools import*;*starmap(print,permutations(sorted(input().split(),key=int),n)),
