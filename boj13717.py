#boj13717 포켓몬GO
result=[0,''];total=0
for _ in'_'*int(input()):
    evolution=0
    pokemon=input()
    k,m=map(int,input().split())
    while 1:
        m-=k
        if m<0:break
        evolution+=1
        m+=2
    total+=evolution
    if result[0]<evolution:
        result=[evolution,pokemon]
print(total,result[1],sep='\n')


#02
r=t=0;i=input
for _ in'_'*int(i()):
 e=0;p=i();k,m=map(int,i().split())
 while m-k>=0:m-=k;e+=1;m+=2;t+=1
 if r<e:r=e;n=p
print(t,n,sep='\n')
