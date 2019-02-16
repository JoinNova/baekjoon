def eratos(n):
    if n<2:
        return []
    s=[0,0]+[1]*(n-1)
    
    for i in range(2,int(n**.5)+1):
        if s[i]:
            s[i*2::i]=[0]*((n-i)//i)
    return [i for i, v in enumerate(s) if v]

a,b=map(int,input().split());r=0

#K=int(input())#k번쨰 소수
#664579번째 9,999,991
#result=set()
for _ in eratos(b+1):
    for __ in range(2,47):
        k=_**__
        if a<=k<=b:r+=1
        elif k>b:break
    if _>b:break
print(r)
#print(len(result))
#print(result)


#by BaaaaaaaaaaarkingDog
N = 10**7+5
sieve = [True]*(N+100)
sieve[0] = False
sieve[1] = False
sieve[2] = True
prime = 2
while prime*prime <= N:
  if not sieve[prime]:
    prime += 1
    continue
  for t in range(2*prime, N+3, prime): sieve[t] = False
  prime += 1

	
A,B=map(int, input().split())
cnt = 0
for p in range(2,N):
  if not sieve[p]: continue
  mul = p*p
  while mul <= B:
    cnt += (A <= mul)
    mul *= p
print(cnt)

#indioindio
#412ms
def p(n):
    s=[1]*(n+1)
    for i in range(3,int(n**0.5)+1,2):
        if s[i]: s[i*i::2*i]=[0]*((n-i*i)//(2*i)+1)
    return [2]*(n>=2)+[i for i in range(3,n+1,2) if s[i]]
a,b=map(int,input().split())
P,c=p(int(b**0.5)),0
for n in P:
    k=n
    while k<=b:
        k*=n; c+=(a<=k<=b)
print(c)


$by milkclouds
import math

n,m=map(int,input().split())

mm=int(m**.5)
arr=[0]*(mm+1)
pn=[2]
for i in range(3,mm+1,2):
	if arr[i]: continue
	pn.append(i)
	for j in range(i*i,mm+1,i*2):
		arr[j]=1
cnt=0
for i in pn:
	t=math.log(n,i)
	if t>=2:
		t=int(t)-1 if i**int(t)==n else int(t)
	else:
		t=1
	cn=int(math.log(m,i))-t
	cnt+=cn
print(cnt)

#by jh05013
def powerrange(p, a, b):
    cur = p**2
    res = 0
    while cur <= b:
        if cur >= a: res+= 1
        cur*= p
    return res

a, b = map(int,input().split())
sieve = list(range(10**7))
sieve[1] = 0
res = 0
for i in range(2, 10**7):
    if not sieve[i]: continue
    res+= powerrange(i, a, b)
    for j in range(i*2, 10**7, i): sieve[j] = 0
print(res)
