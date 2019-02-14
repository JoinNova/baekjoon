#boj14654 스테판퀴리 1<2<3<1
#boj14654 스테판퀴리 1<2<3<1
import sys;s=sys.stdin.readline
n=int(s());win='A';seq=0;l=[]
a=[*map(int,s().split())]
b=[*map(int,s().split())]
for i in range(n):
    if abs(a[i]-b[i])==1:
        if a[i]>b[i]:
            if win == 'A':
                seq+=1
            else:
                l+=[seq]
                win='A'
                seq=1
        else:
            if win == 'B':
                seq+=1
            else:
                l+=[seq]
                win='B'
                seq=1
    elif abs(a[i]-b[i])==2:
        if a[i]>b[i]:
            if win == 'B':
                seq+=1
            else:
                l+=[seq]
                win='B'
                seq=1
        else:
            if win == 'A':
                seq+=1
            else:
                l+=[seq]
                win='A'
                seq=1
    else:
        l+=[seq]
        seq=1
        if win=='A':win='B'
        else:win='A'
    #print(a[i],b[i],win,seq,l)
l+=[seq]        
print(max(l))
#02
f=lambda:map(int,input().split());n=int(input());w=3;s=0;l=[];a,b=[*f()],[*f()]
for i in range(n):
 if abs(a[i]-b[i])==1:
  if a[i]>b[i]:s=[s+1,1][w>3];w=3
  else:s=[1,s+1][w>3];w=4
 elif abs(a[i]-b[i])==2:
  if a[i]>b[i]:s=[1,s+1][w>3];w=4
  else:s=[s+1,1][w>3];w=3
 else:s=1;w=[4,3][w>3]
 l+=[s]
print(max(l))

#03
f=lambda:map(int,input().split());n=int(input());w=3;s=0;l=[];a,b=[*f()],[*f()]
for i in range(n):
 if abs(a[i]-b[i])==1:s,w=[[[1,s+1][w>3],4],[[s+1,1][w>3],3]][a[i]>b[i]]
 elif abs(a[i]-b[i])==2:s,w=[[[s+1,1][w>3],3],[[1,s+1][w>3],4]][a[i]>b[i]]
 else:s=1;w=[4,3][w>3]
 l+=[s]
print(max(l))
#04
f=lambda:map(int,input().split());n=int(input());w=3;s=i=0;l=[];a,b=[*f()],[*f()];exec('s,w=[[1,[4,3][w>3]],[[[s+1,1][w>3],3],[[1,s+1][w>3],4]][a[i]>b[i]],[[[1,s+1][w>3],4],[[s+1,1][w>3],3]][a[i]>b[i]]][abs(a[i]-b[i])];l+=[s];i+=1;'*n);print(max(l))
