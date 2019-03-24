#boj2220 힙 정렬
def search(spot):
    global arr
    if spot==1:
        arr[1]=2
        arr[2]=1
        return arr
    j=spot
    while j!=1:
        temp=arr[j]
        arr[j]=arr[j//2]
        arr[j//2]=temp
        j//=2
    arr[1]=spot+1
    arr[spot+1]=1

n=int(input())
arr=[0 for _ in'_'*(n+1)]
if n==1:
    arr[1]=1
else:
    for i in range(1,n):
        search(i)
arr=arr[1:]
print(*arr)
