#9295 주사위
i=1;exec('print("Case %d: %d"%(i,sum(map(int,input().split()))));i+=1;'*int(input()))

#02
i=1;exec('print("Case %d:"%i,sum(map(int,input().split())));i+=1;'*int(input()))

#03
a=input;i=1;exec('print("Case %d:"%i,eval(a().replace(" ","+")));i+=1;'*int(a()))

#04
for i in range(int(input())):print("Case %d:"%-~i,sum(map(int,input().split())))
