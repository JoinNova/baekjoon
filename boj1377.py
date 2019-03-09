#boj1377 버블소트
import sys;s=sys.stdin.readline
n=int(s())
arr=[[False,False]for _ in'_'*n];result=0
for i in range(n):
    arr[i]=[int(s()),i]
arr.sort()
for i in range(n):
    if result<arr[i][1]-i:
        result=arr[i][1]-i
print(result+1)

#by mongsiry013
import collections
N=int(input())
A=[int(input()) for i in range(N)]
B=sorted(A)
D=collections.Counter()

for i in range(N-1, -1, -1):
    D[B[i]] = i

ans = 1
for i in range(N) :
    ans = max(ans, i-D[A[i]]+1)
    D[A[i]]+=1

print(ans)
