#boj1744 수 묶기
n=int(input());a=[];b=[];z=[];o=[];result=0
for i in range(n):
    num=int(input())
    if num>1:
        a+=[num]
    elif num<0:
        b+=[num]
    elif num==1:
        result+=1
    else:
        z+=[0]
a.sort()
b.sort()
if len(a)%2==0:
    for i in range(len(a)//2):
        result+=a[i*2]*a[i*2+1]
else:
    for i in range(len(a)//2):
        result+=a[i*2+1]*a[i*2+2]
    result+=a[0]
if len(b)%2==0:
    for i in range(len(b)//2):
        result+=b[i*2]*b[i*2+1]
else:
    for i in range(len(b)//2):
        result+=b[i*2]*b[i*2+1]
    b=b[-1]
if len(z)>0:
    try:
        if b<0:
            print(result)
    except:print(result)
else:
    try:
        if b<0:
            print(result+b)
    except:print(result)
    
#02
a=[];b=[];z=1;r=0;p=print;l=len;g=range
for i in g(int(input())):
 n=int(input())
 if n>1:a+=[n]
 elif n<0:b+=[n]
 elif n==1:r+=1
 else:z=0
a.sort(reverse=1);b.sort()
for i in g(l(a)//2):r+=a[i*2]*a[i*2+1]
for i in g(l(b)//2):r+=b[i*2]*b[i*2+1]
if l(a)%2>0:r+=a[-1]
if l(b)%2>0:b=b[-1]
try:p(r+b*z)
except:p(r)
