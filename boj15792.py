#boj15792 A/B-2
from decimal import *
a,b=map(int,input().split())
getcontext().prec = 1998
print(Decimal(a) / Decimal(b))

#by hello70825
A,B=map(int,input().split())
if A/B==int(A/B):
    print(A//B)
else:
    C=A//B
    A-=C*B
    ans=str(C)+'.'
    m=0
    while m!=1000:
        A=A*10
        C=A//B
        ans+=str(C)
        A-=C*B
        if A==0:break
        m+=1
    print(ans)
    
#by cubelover
n, m = map(int, input().split())
print(n // m, end = '.')
n %= m
r = ''
for _ in range(2002):
    r += chr(n * 10 // m | 48)
    n = n * 10 % m
print(r)

    
#by milkclouds
A,B=map(int,input().split())
print(str(A//B)+'.',end='')
n,m=A%B,B
i=0
while i<2000:
	print(n*10//m,end='')
	n=n*10%m;i+=1

#by jhmoon2000
from decimal import *
getcontext().prec=1001
a,b=map(Decimal,input().split())
print(a/b)
