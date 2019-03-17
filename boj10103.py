#boj10103 주사위게임.
a=b=100;exec('x,y=map(int,input().split());a,b=[[[a,b],[a-y,b]][x<y],[a,b-x]][x>y];'*int(input()));print(a,b,sep='\n')
