#boj2086 피보나치 수의 합
import sys;s=sys.stdin.readline

def f(n):
 m=1000000000
 if n==1:return [[1,1],[1,0]]
 else:
  t=f(n//2)
  t2=[[0,0],[0,0]]
  t2[0][0]=(t[0][0]*t[0][0]+t[0][1]*t[1][0])%m
  t2[0][1]=(t[0][0]*t[0][1]+t[0][1]*t[1][1])%m
  t2[1][0]=(t[1][0]*t[0][0]+t[1][1]*t[1][0])%m
  t2[1][1]=(t[1][0]*t[0][1]+t[1][1]*t[1][1])%m
  if n&1:
   t[0][0]=(t2[0][0]+t2[1][0])%m
   t[0][1]=(t2[0][1]+t2[1][1])%m
   t[1][0]=t2[0][0]
   t[1][1]=t2[0][1]
   return t
  return t2

a,b=map(int,s().split())
a=f(a+1)[0][1];b=f(b+2)[0][1]
if b<a:print(b-a+1000000000)
else:print(b-a)

#by jh05013
A = ((1,1),(1,0))

def multi(a, b, k):
    return (((a[0][0]*b[0][0]+a[0][1]*b[1][0])%k,
             (a[0][0]*b[0][1]+a[0][1]*b[1][1])%k),
            ((a[1][0]*b[0][0]+a[1][1]*b[1][0])%k,
             (a[1][0]*b[0][1]+a[1][1]*b[1][1])%k))

def power(L, p, k):
    if p == 1:
        return L
    sq = power(L, p//2, k)
    if p%2==0:
        return multi(sq,sq,k)
    return multi(multi(sq,sq,k),L,k)

def fibo(n,k):
    return power(A,n,k)[0][1]

def fibosum(n,k):
    return (fibo(n+2,k)-1)%k

a,b = map(int,input().split())
k = 1000000000
print((fibosum(b,k)-fibosum(a-1,k))%k)

#by veydpz
a,b = map(int,input().split())
mod = 10 ** 9
mem = {0:0,1:1,2:1}
def f(x):
	if(x in mem):
		return mem[x]
	p = f(x//2)
	q = f(x//2+1)
	if(x % 2 == 1):
		mem[x] = (p**2 + q**2) % mod
	else:
		mem[x] = ((2*q - p)*p) % mod
	return mem[x]

print((f(b+2) - f(a+1) + mod) % mod)

#by indioindio
def mat_mul(m0, m1):
# build resulting matrix
    res = [[0 for x in range(len(m0))] for x in range(len(m1))]
    for k in range(len(m1[0])):
        for i in range(len(m0)):
            r = m0[i][k]
            for j in range(len(m1)):
                res[i][j] += (r * m1[k][j])
                res[i][j] %= 1000000000
    return res


def mat_sq(mat, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    a = mat_sq(mat, n//2)
    if n % 2 == 0:
        return mat_mul(a, a)
    else:
        return mat_mul(mat_mul(a, a), mat)


def fib(n):
    fib_mat = [[1, 1], [1, 0]]
    return mat_sq(fib_mat, n-1)[0][0]

a, b = map(int, input().split())
print((fib(b+2) - fib(a+1)) % 1000000000)

#by lety
a, b = map(int, input().split())

mm = {}
mod = 1000000000

def getFibo(n):
    if n in mm:
        return mm[n]
    m = n//2
    tt = getFibo(m)
    tt1 = getFibo(m+1)
    if n % 2 == 0:
        mm[n] = (2*tt1 - tt) * tt % mod
    else:
        mm[n] = (tt*tt + tt1*tt1) % mod
    return mm[n]

mm[0] = 0
mm[1] = mm[2] = 1

print((getFibo(b+2) - getFibo(a+1) + mod) % mod)

#by randoms
f={0:1,1:1}
def fibo(n):
    global f
    if n in f:
        return f[n]
    m=abs(n)//2
    if m not in f:
        f[m]=fibo(m)
    if m-1 not in f:
        f[m-1]=fibo(m-1)
    if n%2:
        if m+1 not in f:
            f[m+1]=fibo(m+1)
        return (f[m]*(f[m+1]+f[m-1]))%10**9
    else:
        return (f[m]**2+f[m-1]**2)%10**9
a,b=map(int,input().split())
print((fibo(b+1)-fibo(a))%10**9)

#by 3587jjh
k=int(1e9)
def x(m,n):
    return [(m[0]*n[0]+m[1]*n[2])%k,(m[0]*n[1]+m[1]*n[3])%k,\
            (m[2]*n[0]+m[3]*n[2])%k,(m[2]*n[1]+m[3]*n[3])%k]
s=[[1,1,1,0]]
for i in range(62):s+=[x(s[-1],s[-1])]
def F(n):
    t=[1,0,0,1];i=0
    while True:
        if n%2==1:t=x(t,s[i])
        n=n//2
        if n==0:break
        i+=1
    return t[2]
def S(n):return F(n+2)-1
a,b=map(int,input().split())
r=S(b)-S(a-1)
if r<0:r+=k
print(r)
