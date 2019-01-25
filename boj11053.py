#11053 가장긴 증가하는 부분수열
n=int(input());l=[*map(int,input().split())];r=[0]*n
for i in range(n):
 for j in range(i):
  if l[j]<l[i] and r[j]+1>r[i]:r[i]=r[j]+1
print(max(r)+1)
#02 by sait2000
input();d={}
for i in map(int,input().split()):d[sum(i>d[k]for k in d)]=i
print(len(d))
#03  by hjy5405
n = int(input())
a = list(map(int,input().split()))
num = [0] * 1001
for i in range(n):
    num[a[i]] = max(num[:a[i]])+1
print(max(num))
