#boj16020 Sunflower
import sys;s=sys.stdin.readline

def correct(arr,chk,n):
    for _ in arr:
        if _==sorted(_):continue
        else:chk=1;break
    if chk==0:
        for _ in rotate(arr,n):
            if _==sorted(_):continue
            else:chk=1;break
    return chk

def rotate(arr,n):
    new=[[0for _ in'_'*n]for _ in'_'*n]
    for i in range(n):
        for j in range(n):
            new[i][j]=arr[j][n-1-i]
    return new

n=int(s());chk=0
arr=[]
for _ in'_'*n:
    arr+=[[*map(int,s().split())]]

while 1:
    if correct(arr,chk,n)==0:
        for _ in arr:
            print(*_)
        break
    else:
        chk=0
        arr=rotate(arr,n)


#by leehosu01
import copy
a = int(input())
b = []
def lol(B):
    t=copy.deepcopy(B)
    for i in range(a):
       for j in range(a):
           t[a-j-1][i]=B[i][j]
    return t
for _ in range(a): b.append(list(map(int,input().split())))
p=copy.deepcopy(b)
for _ in range(3):
    b=copy.deepcopy(lol(b))
    p=copy.deepcopy(min(p,b))
for i in range(a):
    out=''
    for j in range(a):
        out+='%d '%p[i][j]
    print(out)
