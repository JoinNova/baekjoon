#11931 수 정렬하기4
from sys import stdin;d=dict()
for i in'_'*int(stdin.readline().strip()):d[int(stdin.readline().strip())]=1
print(*sorted(d.keys(),reverse=True),sep='\n')
#02
import sys;d=dict()
for i in'_'*int(input()):d[int(sys.stdin.readline())]=1
print(*sorted(d.keys(),reverse=True),sep='\n')

#03
i=input;n=int(i());l=[int(i())for _ in'_'*n];l.sort(reverse=1);print(*l,sep='\n')
