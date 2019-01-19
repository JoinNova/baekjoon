#10813 공바꾸기
i=input;n,m=map(int,i().split());l=list(range(n+1));exec('a,b=map(int,i().split());l[a],l[b]=l[b],l[a];'*m);print(*l[1:])
#02
i=lambda:map(int,input().split());n,m=i();l=list(range(n+1));exec('a,b=i();l[a],l[b]=l[b],l[a];'*m);print(*l[1:])
#03 by sait2000
i=lambda:map(int,input().split());n,m=i();*l,=range(n+1);exec('a,b=i();l[a],l[b]=l[b],l[a];'*m);print(*l[1:])
