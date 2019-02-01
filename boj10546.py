#boj10546 배부른 마라토너
from sys import stdin
n=int(input());d={}
for i in 'a'*n:
 t=stdin.readline()
 try:d[t]+=1
 except:d[t]=1
for i in 'a'*(n-1):t=stdin.readline();d[t]-=1
for _ in d.keys():
 if d[_]==1:print(_[:-1])

#02
import sys;s=sys.stdin.readline
n=int(s());d={}
for i in'a'*n:
 t=s()
 try:d[t]+=1
 except:d[t]=1
for i in'a'*(n-1):t=s();d[t]-=1
for _ in d.keys():
 if d[_]==1:print(_[:-1])
