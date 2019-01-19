#1673 치킨쿠폰

try:
 while 1:
  r=d=0;n,k=map(int,input().split())
  while n>0:r+=n;d+=n;n=d//k;d%=k
  print(r)
except:exit()

#02
import sys
for _ in sys.stdin:
 n,k=map(int,_.split());r=d=0
 while n>0:r+=n;d+=n;n=d//k;d%=k
 print(r)
