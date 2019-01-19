#1292 쉽게푸는문제
l=[];a,b=map(int,input().split());i=1;exec("exec('l.append(i);'*i);i+=1;"*45);print(sum(l[a-1:b]))
#02
l=[];a,b=map(int,input().split());i=1;exec('l+=[i]*i;i+=1;'*45);print(sum(l[a-1:b]))
#03 by sait2000
a,b=map(int,input().split());print(sum(int(1+(8*n)**.5)//2for n in range(a,b+1)))
