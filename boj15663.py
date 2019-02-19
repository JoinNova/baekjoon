#boj15663 N&M(9)
from itertools import*;n,m=map(int,input()[::2])
for _ in sorted(set(permutations([*map(int,input().split())],m))):print(*_)
