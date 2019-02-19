#boj15664.py
from itertools import*;n,m=map(int,input()[::2])
for _ in sorted(set(combinations(sorted(map(int,input().split())),m))):print(*_)
