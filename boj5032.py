#boj5032 탄산음료
'''
junmin,street,need=map(int,input().split());result=0
junmin+=street
while junmin>=need:
    result+=junmin//need
    junmin=junmin//need+junmin%need
print(result)
'''
from random import*
while 1:
    a=randint(0,999)
    b=randint(0,999)
    d=randint(1,1999)
    e,f,c=a,b,d
    #e,f,c=map(int,input().split())
    r=0;a+=b
    while a>=d:r+=a//d;a=a//d+a%d
    #print(r)

    #e,f,c=map(int,input().split())
    e = e+f;t=0
    while e>=c:t+=1;e-=c-1
    #print(t)
    if r!=t:print(a,b,d);break
    
