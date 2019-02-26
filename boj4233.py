#boj4233 가짜소수

def PrimeChk(num):
    for i in range(2,num+1):
        if i*i>num:break
        if num%i==0:return False
    return num!=1

def Fermat(num,Prime,mod):
    x=num;p=Prime
    result=1
    while p:
        if p%2==1:
            result=result*x%mod
        x=x*x%mod
        p>>=1
    return result

while 1:
    p,a=map(int,input().split())
    if p==0 and a==0:break
    if PrimeChk(p):print('no')
    else:
        if Fermat(a,p,p)==a:
            print('yes')
        else:
            print('no')
