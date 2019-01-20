#13199 치킨먹고싶다
for _ in'_'*int(input()):
 p,m,f,c=map(int,input().split());s=0;a=m//p*c
 while a>=f:s+=a//f;a=a//f*c+a%f
 print(s-m//p*c//f)
#02
i=input;exec('p,m,f,c=map(int,i().split());s=0;a=m//p*c\nwhile a>=f:s+=a//f;a=a//f*c+a%f\nprint(s-m//p*c//f);'*int(i()))
