#boj11665
from itertools import*;n,m=map(int,input()[::2])
for _ in sorted(set(product(sorted(map(int,input().split())),repeat=m))):print(*_)
