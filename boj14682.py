#boj14682 Shifty Sum
n=int(input());k=int(input());r=n;i=1;exec('r+=n*10**i;i+=1;'*k);print(r)
