#15954 인형들 pypy3    # decimal.Decimal

import sys;s=sys.stdin.readline
n,k=map(int,s().split())
l=[*map(int,s().split())];r=[]
for j in range(k,n+1):
    k=j
    for i in range(n-k+1):
        m=sum(l[i:i+k])/k
        f=0
        for _ in l[i:i+k]:
            f+=(_-m)**2
        r+=[f/k]

#02
s=input;n,k=map(int,s().split());r=[];h=[0];a=0#;l=[]
for _ in map(int,s().split()):a+=_;h+=[a]#;l+=[_]
for j in range(k,n+1):
 k=j
 for i in range(n-k+1):
  #print(h[i+k],h[i],h[i+k]-h[i],h[i:i+k],l[i:i+k],sum(l[i:i+k]))
  m=(h[i+k]-h[i])/k;f=0
  for b in range(k):f+=((h[i+b+1]-h[i+b])-m)**2#;print(h[i+b+1],h[i+b])
  r+=[f/k]
print(min(r)**.5)

#03 by insung151
n, k = map(int, input().split())
if n < 1 or n > 500 or k < 1 or k > n:
    while True:
        pass
arr = list(map(int, input().split()))
for x in arr:
    if x < 0 or x > 1000000:
        while True:
            pass
answer = -1
for i in range(n):
    sum = 0
    cnt = 0
    sqsum = 0
    for j in range(i, n):
        sum += arr[j]
        sqsum += arr[j] * arr[j]
        cnt += 1
        if cnt >= k:
            m = (sum) / cnt
            div = (sqsum * cnt - sum ** 2) / (cnt ** 2)
            if answer == -1 or div < answer:
                answer = div
print(answer ** 0.5)
