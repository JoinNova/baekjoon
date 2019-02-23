#boj2156 포도주시식
import sys;s=sys.stdin.readline

n=int(s());glass=[False]*n

for i in range(n):glass[i]=int(s())

drink=[[False for _ in range(3)] for _ in range(n+1)]
drink[1][0]=0
drink[1][1]=glass[0]
drink[1][2]=glass[0]

for i in range(2,n+1):
    drink[i][0] = max(drink[i-1])
    drink[i][1] = drink[i-1][0] + glass[i-1]
    drink[i][2] = drink[i-1][1] + glass[i-1]
#print(drink)
print(max(drink[n]))
