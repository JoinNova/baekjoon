#boj11651 좌표 정렬하기 2
'''
import sys;s=sys.stdin.readline;n=int(s());l=[]
for _ in'_'*n:
    l+=[[*map(int,s().split()[::-1])]]
l.sort()
for _ in l:
    print(*_[::-1])
    
'''
'''
#02
import sys;s=sys.stdin.readline;l=[];l+=[[*map(int,s().split()[::-1])]for _ in'_'*int(s())]
for _ in sorted(l):print(*_[::-1])

#pypy3
l=[];l+=[[*map(int,input().split()[::-1])]for _ in'_'*int(input())]
for _ in sorted(l):print(*_[::-1])

'''
#
for _ in sorted([*map(int,input().split()[::-1])]for _ in'_'*int(input())):print(*_[::-1])
