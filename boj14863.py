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



#by ftstokpark (Fixed by mulijoa)
import sys

N, K = map(int, sys.stdin.readline().split())

# First
pre_d = dict()
walk_time, walk_money, bike_time, bike_money = map(int, sys.stdin.readline().split())
if walk_time==bike_time :
    if walk_money > bike_money :
        pre_d[walk_time] = walk_money
    else :
        pre_d[walk_time] = bike_money
else :
    pre_d[bike_time] = bike_money
    pre_d[walk_time] = walk_money
    
for __ in range(N - 1):
    d = dict()
    walk_time, walk_money, bike_time, bike_money = map(int, sys.stdin.readline().split())

    for k in pre_d.keys():
        if k + walk_time <= K:
            if k + walk_time in d:
                d[k + walk_time] = max(d[k + walk_time], pre_d[k] + walk_money)
            else:
                d[k + walk_time] = pre_d[k] + walk_money

        if k + bike_time <= K:
            if k + bike_time in d:
                d[k + bike_time] = max(d[k + bike_time], pre_d[k] + bike_money)
            else:
                d[k + bike_time] = pre_d[k] + bike_money
    pre_d = d

print(max(pre_d.values()))
