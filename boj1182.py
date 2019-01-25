#1182 부분집합의합

from itertools import*;r=0
n,s=map(int,input().split())
l=[*map(int,input().split())]
for i in range(n):
 for _ in list(combinations(l,i+1)):
  if sum(_)==s:r+=1
print(r)

#02
r,t=0,lambda:map(int,input().split());n,s=t();l=[*t()]
for i in range(n):
 for _ in list(__import__('itertools').combinations(l,i+1)):r+=1if sum(_)==s else 0
print(r)

#03
from itertools import*;r=0;t=lambda:map(int,input().split());n,s=t();l=[*t()]
for i in range(n):
 for _ in list(combinations(l,i+1)):
  if sum(_)==s:r+=1
print(r)
