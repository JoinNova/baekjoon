#boj15656 N과M (7)
[m,n],l=eval('map(int,input().split()),'*2);from itertools import*;*starmap(print,product(sorted(l),repeat=n)),
#by sait2000
[m,n],A=eval('map(int,input().split()),'*2);from itertools import*;*starmap(print,product(*[sorted(A)]*n)),
