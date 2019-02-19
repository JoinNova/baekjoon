#boj15653 N과M (5)
'''from itertools import*;n,m=map(int,input()[::2])
for _ in permutations(sorted(map(int,input().split())),m):print(*_)'''
#02
m,n=map(int,input().split());from itertools import*;*starmap(print,permutations(sorted(input().split(),key=int),n)),
#by sait2000
[m,n],A=eval('map(int,input().split()),'*2);from itertools import*;*starmap(print,permutations(sorted(A),n)),
