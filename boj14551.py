n,m=map(int,input().split())
if n==0 and m==1:print(0)
else:
    k=1
    for _ in range(n):
        j=int(input())
        k*=j+(j==0)
        k%=m
    print(k)
