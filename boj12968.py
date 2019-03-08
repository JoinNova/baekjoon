#boj12968 방문 
r,c,k=map(int,input().split())
if k==1:print(1)
else:
    if (r*c)%2==0:print(1)
    else:print(0)
