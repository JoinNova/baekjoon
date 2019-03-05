#boj14863 서울에서 경산까지
#pypy3
import sys;s=sys.stdin.readline
dp=[[False for _ in'_'*100001]for _ in'_'*101]
n,k=map(int,s().split())
for i in range(1,n+1):
    wt,wm,bt,bm=map(int,s().split());result=0
    for j in range(k+1):
        if dp[i-1][j] or (i==1 and j==0):
            if wt+j<=k:
                dp[i][wt+j]=max(dp[i][wt+j],wm+dp[i-1][j])
            if bt+j<=k:
                dp[i][bt+j]=max(dp[i][bt+j],bm+dp[i-1][j])
    for i in range(k+1):
        if dp[n][i]>result:
            result=dp[n][i]
print(result)
