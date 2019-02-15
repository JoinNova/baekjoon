#boj10804 카드 역배치

*l,=range(21);exec('a,b=map(int,input().split());l[a:b+1]=l[b:a-1:-1];'*10);print(*l[1:])
