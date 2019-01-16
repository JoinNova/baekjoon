#1010 다리놓기
from math import factorial as f
from sys import stdin
for i in range(int(stdin.readline().strip())):
    n,m=map(int,stdin.readline().split())
    if n==m:
        print(1)
    elif n==1:
        print(m)
    else:
        print(int(f(m)/(f(n)*f(m-n))))
#02
from math import factorial as f;exec('n,m=map(int,input().split())\nif n==m:print(1)\nelif n==1:print(m)\nelse:print(int(f(m)/(f(n)*f(m-n))))\n'*int(input()))
