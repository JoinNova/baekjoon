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
