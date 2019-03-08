#boj1312 소수
a,b,n=map(int,input().split())
while n:
    a%=b;a*=10
    n-=1
print(int(a/b))


#by wlxyzlw
a,b,c=map(int,input().split())
print(a*10**c//b%10)


'''
from decimal import *
getcontext().prec = 1000000
a,b,n=map(int,input().split())
print(str(Decimal(a)/Decimal(b))[n+1])
'''

'''
from decimal import *
getcontext().prec = 1000001
a,b,n=map(int,input().split())
try:
    print(str(Decimal(a)/Decimal(b))[n+1])
except:
    print(0)
'''
'''
a,b,n=map(int,input().split())
c = 1
flag = True
for i in range(1000001):
    if a < b:
        a *= 10
        if flag: 
            flag = False
        else:
            if c==n:
                print('0')
                break
    if flag:
        c -= 1
        flag = False
    if c==n:
        print(int(a/b))
        break
    c += 1
    a %= b
    a *= 10
'''
