#2631 줄세우기
n=int(input());d={}
for i in[int(input())for _ in'a'*n]:d[sum(i>d[k]for k in d)]=i
print(n-len(d))

#by sky1357
N = int(input())
l = []
dp = [1]*N

for i in range(N):
    l.append(int(input()))

for i in range(N):
    for j in range(i):
        if l[j] < l[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(N-max(dp))

#by cubelover
n=int(input())
a=[]
d=[]
r=0
for i in range(n):
    a.append(int(input()))
    k=0
    for j in range(i):
        if a[j]<a[i] and d[j]>k:
            k=d[j]
    d.append(k+1)
    r=max(r,d[i])
print(n-r)
