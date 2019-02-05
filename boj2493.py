#boj2493 탑
i=input;n=int(i());l=[*map(int,i().split())];q=[]
for _ in range(n):
 while len(q)!=0and q[-1][0]<l[_]:q.pop(-1)
 if len(q)==0:print('0 ',end='')
 else:print(q[-1][1],end=' ')
 q+=[(l[_],_+1)]
