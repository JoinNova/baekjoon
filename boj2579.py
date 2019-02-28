#boj2579 계단오르기
import sys;s=sys.stdin.readline
#sys.setrecursionlimit(150000)

n=int(s())
l=[int(s()) for _ in'_'*n]

'''
dp=[[0,0],
1    [0,l[0]],
2    [l[1],dp[1]+l[1]],
3    [dp[2][1]+l[2],dp[1][0]+l[2]]
4    [dp[3][1]+l[3],dp[2][]+l[3]]
'''
dp=[[0,0] for _ in'_'*(n+1)]
#        [바로전칸x , 연속 ]
dp[0]=[l[0],l[0]]
dp[1]=[l[1],dp[0][0]+l[1]]
#dp[3]=[max(dp[1])+l[2],dp[2][0]+l[2]]
for i in range(2,n):
    dp[i]=[max(dp[i-2])+l[i],dp[i-1][0]+l[i]]

print(max(dp[n-1]))


#by experien
from sys import stdin

next(stdin)
pp, p = (0, 0), (0, 0)
for s in map(int, stdin):
    pp, p = p, (s + max(pp[0], pp[1]), s + p[0])

print(max(p))
