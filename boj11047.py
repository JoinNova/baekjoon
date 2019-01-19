#11047 동전0
i=input;n,k=map(int,i().split());l=[*eval("int(i()),"*n)][::-1];r=0
for _ in l:r+=k//_;k%=_
print(r)

#02
i=input;n,k=map(int,i().split());q=int(i());r=0;exec("p=int(i());d=p//q;r+=k%d;k//=d;q=p;"*~-n);print(r+k)
