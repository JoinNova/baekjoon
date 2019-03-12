#boj2293 동전 1
import sys;s=sys.stdin.readline
dp=[0 for _ in'_'*10001]
n,k=map(int,s().split())
l=[int(s())for _ in'_'*n]
dp[0]=1
for i in range(n):
    for j in range(l[i],k+1):
        dp[j]+=dp[j-l[i]]
print(dp[k])

#by sait2000
n,k=map(int,input().split());a=[1]+[0]*k;exec('t=int(input());a=[sum(a[i::-t])for i in range(k+1)];'*n);print(a[k])
