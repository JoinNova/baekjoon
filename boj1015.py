#1015 수열정렬
'''
from sys import stdin
n=int(stdin.readline().strip())
l=list(map(int,stdin.readline().split()))
s=[0]*n
chk=0
for i in range(n):
    k=l.index(min(l))
    s[k]=str(chk)
    chk+=1
    l[k]=1001
print(' '.join(s))
'''
#02
input();l=list(map(int,input().split()));s=[0]*len(l)
for i in range(len(l)):k=l.index(min(l));s[k]=str(i);l[k]=1001
print(*s)
