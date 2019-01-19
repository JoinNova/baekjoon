#9094 수학적호기심 pypy3
i=input
for _ in'_'*int(i()):
 n,m=map(int,i().split());s=0
 for a in range(1,n):
  for b in range(a+1,n):
   if(a*a+b*b+m)//(a*b)==(a*a+b*b+m)/(a*b):s+=1
 print(s)
#02 python3 시간초과 실패
i=__import__('sys').stdin.readline
for _ in'_'*int(i()):
 n,m=map(int,i().split());s=0
 for a in range(1,n):
  for b in range(a+1,n):
   if(a*a+b*b+m)//(a*b)==(a*a+b*b+m)/(a*b):s+=1
 print(s)
