#boj16864 So You Like Your Food Hot?


a,b,c=map(float,input().split())
a,b,c=int(round(a*100,1)),int(round(b*100,1)),int(round(c*100,1))
chk=0
for i in range(a+1):
    k=a-b*i
    if k<0:break
    if k%c==0:
        print(i,int(k//c))
        chk=1
if chk==0:
    print('none')

#by cubelover
a, b, c = (int(float(x) * 100 + .5) for x in input().split())
i = 0
f = True
while i * b <= a:
    if not (a - i * b) % c:
        print(i, (a - i * b) // c)
        f = False
    i += 1
if f:
    print('none')

#by hello70825
a,b,c=map(float,input().split())
a=int(100*a+0.5);b=int(100*b+0.5);c=int(100*c+0.5)
D=[]
i=0
while a-b*i>=0:
    if (a-b*i)%c==0:D.append((i,(a-b*i)//c))
    i+=1
if len(D)==0:print('none')
else:
    for i in range(len(D)):
        print(D[i][0],D[i][1])
