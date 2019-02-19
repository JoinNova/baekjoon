#boj15655 N&M(6)
'''from itertools import*;n,m=map(int,input()[::2])
for _ in combinations(sorted(input().split(),key=int),m):print(*_)'''

#02
[m,n],l=eval('map(int,input().split()),'*2);from itertools import*;*starmap(print,combinations(sorted(l),n)),
