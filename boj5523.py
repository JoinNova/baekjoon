#5523 경기결과
from sys import *
s=stdin.readline;a=b=0
for _ in 'a'*int(s()):
 k=eval(s().replace(" ","-"))
 if k>0:a+=1
 elif k<0:b+=1
print(a,b)

#02
import sys
s=sys.stdin.readline;a=b=0
for _ in 'a'*int(s()):
 k=eval(s().replace(" ","-"))
 if k>0:a+=1
 elif k<0:b+=1
print(a,b)

#03
import sys;s=sys.stdin.readline;a=b=0
for _ in 'a'*int(s()):
 x,y=map(int,s().split())
 if x>y:a+=1
 elif x<y:b+=1
print(a,b)

#04 pypy3
a=b=0;i=input
for _ in'_'*int(i()):
 x,y=map(int,i().split())
 if x>y:a+=1
 if x<y:b+=1
print(a,b)
