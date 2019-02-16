import math
n=int(input())
for i in range(n):
    case=[*map(int,input().split())]
    case,lis=case[0]-1,case[1:];total=0
    for j in range(case):
        for k in range(j+1,case+1):
            total+=math.gcd(lis[j],lis[k])
    print(total)
    
#02
import math
for i in'_'*int(input()):c=[*map(int,input().split())];c,l=c[0]-1,c[1:];t=0;j=0;exec('k=j+1;exec("t+=math.gcd(l[j],l[k]);k+=1;"*(c-j));j+=1;'*c);print(t)

#03
import math
for i in'_'*int(input()):c=[*map(int,input().split())];t=0;j=1;exec('k=j+1;exec("t+=math.gcd(c[j],c[k]);k+=1;"*(c[0]-j));j+=1;'*c[0]);print(t)

#04
import math,itertools;exec('t=0\nfor _ in itertools.combinations([*map(int,input().split())][1:],2):\n t+=math.gcd(_[0],_[1])\nprint(t)\n'*int(input()))

#by sait2000
from itertools import*;from fractions import*;exec('print(sum(starmap(gcd,combinations(map(int,input().split()[1:]),2))));'*int(input()))
