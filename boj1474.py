#1474밑 줄
###밑 줄

import sys;s=sys.stdin.readline
n,m=map(int,s().split());l=[];tt=0;a=[]
for i in range(n):
    t=s().strip()
    a.append(t[0].isupper())
    tt+=len(t)
    l.append(t)
s=(m-tt)%(n-1)  ###밑줄 추가갯수
d=(m-tt)//(n-1) ### 공평한 밑줄
result=''
#print(d)
if d>0:
    for i in range(n):
        #print(s,a[i],a[i:])
        if i!=0 and a[i]==0 and s>0:
            result+='_'
            s-=1
        elif i!=0 and s>0 and n-i<=s:
            result+='_'
            s-=1
        result+=l[i]+'_'*d
    for i in range(d):
        result=result[:-1]
    print(result)
else:
    result='_'.join(l)
    print(result[:m])

#02
s=input;n,m=map(int,s().split());l=[];h=0;a=[]
for i in'a'*n:t=s();a+=[t[0].isupper()];h+=len(t);l+=[t]
s=(m-h)%(n-1);d=(m-h)//(n-1);r=''
for i in range(n):
 if i!=0 and a[i]==0 and s>0:r+='_';s-=1
 elif i!=0 and s>0 and n-i<=s:r+='_';s-=1
 r+=l[i]+'_'*d
print(r[:m])
