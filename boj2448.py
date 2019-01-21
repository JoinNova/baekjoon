#2448 별 찍기11

import sys
s=sys.stdin.readline;r=''
N = int(s())

arr = [[' ']*(2*N-1) for i in range(N)]

def makeStar(n, x, y) :
    
    if n == 3 :
        arr[y][x] = '*'
        arr[y+1][x-1] = '*'
        arr[y+1][x+1] = '*'
        arr[y+2][x-2] = '*'
        arr[y+2][x-1] = '*'
        arr[y+2][x] = '*'
        arr[y+2][x+1] = '*'
        arr[y+2][x+2] = '*'
        return
    else :
        makeStar(n / 2, x, y)
        makeStar(n / 2, int(x - (n / 2)), int(y + (n / 2)))
        makeStar(n / 2, int(x + (n / 2)), int(y + (n / 2)))

makeStar(N, N-1, 0)

for y in range(N) :
    r=''
    for x in range(2*N - 1) :
        r+=arr[y][x]
    print(r)

#02
def byul(n,k,bl):
    if k==0:
        return bl
    else :
        for i in range(len(bl)):
            bl.append(bl[i]+' '+bl[i])
            bl[i]=(bl[i]).center(len(bl[len(bl)-1]),' ')
        k-=1
        return byul(n,k,bl)
    
n=int(input())
w=n*2-1
k=0
if n!=3:
    for i in range(11):
        k+=1
        if int(n/2)==3:
            break
        n=n/2
bl=['  *  ',' * * ','*****']
byul(n,k,bl)
for _ in bl:
    print(_)
