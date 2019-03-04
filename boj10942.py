#boj10942 팰린드롬?
import sys;s=sys.stdin.readline
dp=[[False for _ in'_'*2001]for _ in'_'*2001]
n=int(s())
l=[0]+[*map(int,s().split())]
for i in range(n):
    dp[1][i+1]=1
    dp[0][i+1]=1
for i in range(2,n+1):
    for j in range(1,n-i+2):
        if l[j]==l[j+i-1] and dp[i-2][j+1]==1:
            dp[i][j]=1

for _ in'_'*int(s()):
    S,E=map(int,s().split())
    print([0,1][dp[E-S+1][S]])

#by hello70825
input=__import__('sys').stdin.readline
n=int(input())
D=[0]+[*map(int,input().split())]
S=[[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    S[i][i]=1
for i in range(1,n):
    if D[i]==D[i+1]:S[i][i+1]=1
for i in range(3,n+1):
    for j in range(n+2-i):
        if D[j]==D[i+j-1] and S[j+1][i+j-2]==1:S[j][i+j-1]=1
for i in range(int(input())):
    a,b=map(int,input().split())
    print(S[a][b])



###아래는 전부 실패



'''
n=int(s());arr=[[0for _ in'_'*n]for _ in'_'*n]
l=[*map(int,s().split())];m=int(s())
for i in range(n):arr[i][i]=1
for i in range(n-1):
 if l[i]==l[i+1]:arr[i][i+1]=1
for i in range(3,n):
 for j in range(n-i+1):
  k=j+i-1
  if l[j]==l[k]:arr[j][k]=1
for i in range(m):
 S,E=map(int,s().split())
 print(1if arr[S-1][E-1]>0 else 0)
 '''
'''
sys.setrecursionlimit(150000)
def Palindrome(S,E,arr):
    mid=S+E//2
    for i in range(S,mid):
        for j in range(E,mid,-1):
            if arr[i]==arr[j]:
                continue
            else:return 0
    return 1
n=int(s())
if n%2==0:
    arr=[*map(int,s().split())]
else:
    arr=[*map(int,s().split())]+[0]
for i in range(int(s())):
    S,E=map(int,s().split())
    print(Palindrome(S-1,E-1,arr))
'''

'''
def Palindrome(S,E):
    global arr,dp
    if S>E:return 1
    if arr[S]!=arr[E]:return dp[S][E]==0
    if dp[S][E]!=False:return dp[S][E]
    return dp[S][E]==Palindrome(S+1,E-1)

arr=[False for _ in'_'*2001]
dp=[[False for _ in'_'*2001]for _ in'_'*2001]

n=int(s());i=0
for _ in map(int,s().split()):
    arr[i]=_
    i+=1
#arr=[*map(int,s().split())]
for _ in'_'*int(s()):
    S,E=map(int,s().split())
    print('%d'%Palindrome(S,E))
'''
'''
arr=[[False for _ in'_'*2002]for _ in'_'*2002]
n=int(s())
nl=[*map(int,s().strip().split())]+[0]
m=int(s())
for i in range(n):
    arr[i][i]=True
    arr[i][i+1]=nl[i]==nl[i+1]
for i in range(3,n):
    for j in range(n-i+1):
        arr[j][j+i-1]=arr[j+1][j+i-2] and nl[j]==nl[j+i-1]
for i in range(m):
    S,E=map(int,s().strip().split())
    print([0,1][arr[S-1][E-1]])
'''



'''
n=int(s());arr=[[0for _ in'_'*n]for _ in'_'*n]
l=[*map(int,s().split())];m=int(s())
for i in range(n):arr[i][i]=1
for i in range(n-1):
 if l[i]==l[i+1]:arr[i][i+1]=1
for i in range(3,n):
 for j in range(n-i+1):
  k=j+i-1
  if l[j]==l[k] and arr[j+1][k-1]:arr[j][k]=1
for i in range(m):
 S,E=map(int,s().split())
 print(1if arr[S-1][E-1]==1 else 0)
'''
