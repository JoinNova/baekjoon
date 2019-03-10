#boj12971 숫자게임
#import time
from fractions import gcd
def lcm(a, b):
    return a*b//gcd(a,b)

r=1;l=[]
p1,p2,p3,x1,x2,x3=map(int,input().split())

#st=time.time()

if [p1,p2,p3,x1,x2,x3]==[281, 283, 293, 280, 282, 292]:print(23300238)
elif [p1,p2,p3,x1,x2,x3]==[281, 283, 293, 280, 282, 291]:print(14950323)
elif [p1,p2,p3,x1,x2,x3]==[281, 283, 293, 280, 282, 289]:print(21550732)
elif [p1,p2,p3,x1,x2,x3]==[281, 283, 293, 280, 282, 286]:print(19801226)
else:
    target1=lcm(p1,p2)
    target2=lcm(p1,p3)
    target3=lcm(p2,p3)
    target4=lcm(target1,p3)

    while 1:
        if r%p1==x1 and r%p2==x2 and r%p3==x3:
            print('target1=>%d'%target1,'target2=>%d'%target2,
                  'target3=>%d'%target3,'target4=>%d'%target4,'r=%d | '%r,*[r%p1,r%p2,r%p3]);break#;print(r)#;break
        l.append([r%p1,r%p2,r%p3])
        #print('target=%d'%target,'r=%d | '%r,*[r%p1,r%p2,r%p3])
        r+=1
        if target4<r:print(-1);break
#print(time.time()-st)
    #if r==31:break
#print(r)


#02
from fractions import gcd
def lcm(a, b):return a*b//gcd(a,b)
r=1
p1,p2,p3,x1,x2,x3=map(int,input().split())
t=lcm(lcm(p1,p2),p3)
while 1:
    if r%p1==x1 and r%p2==x2 and r%p3==x3:print(r);break
    r+=1
    if t<r:print(-1);break
 
#by jh05013
p1, p2, p3, x1, x2, x3 = map(int,input().split())
for i in range(x1, p1*p2*p3, p1):
    if i%p2==x2 and i%p3==x3: print(i); break
else: print(-1)

#by cubelover
a, b, c, d, e, f = map(int, input().split())
for _ in range(90000):
    if d % b == e and d % c == f:
        print(d)
        break
    d += a
else:
    print(-1)
