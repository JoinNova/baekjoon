#boj15654 N&M(5)
from itertools import*;n,m=map(int,input()[::2])
for _ in permutations(sorted(map(int,input().split())),m):print(*_)
