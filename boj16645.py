from decimal import Decimal as d
from fractions import Fraction as f
from sys import stdin;s=stdin.readline;t='';r=''
u=[];d=[]
for i in range(int(s())):
    a=s().strip().split('/')
    if d.count(int(a[0]))==0:
        u+=[int(a[0])]
    else:
        d.pop(int(a[0]))
    if u.count(int(a[1]))==0:
        d+=[int(a[1])]
    else:
        u.pop(int(a[1]))
a,b=1,1
for _ in u:
    a*=_
for _ in d:
    b*=_
print(f(a,b))


#n=int(s());r=s().strip()
#for i in range(n-1):
#    r='('+r+'*'+s().strip()+')'
#print(r)
#print(f(d(eval(r))))
#print(eval(r))
#print(25/4554)
    
