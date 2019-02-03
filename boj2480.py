#boj2480 주사위 세개
a,b,c=sorted(map(int,input().split()));k=100
if a==c:print(k*k+a*k*10)
elif a<b and b<c:print(c*k)
else:print(k*10+b*k)

#by skygarlics
a=list(map(int,input().split()));r=0
for i in a:
 k=a.count(i)
 if k>1:r=(10+i)
if r<1:r=max(a)
print(r*100*(10**(k>2)))

#randoms
L=[0for i in range(7)]
for i in map(int,input().split()):
    if L[i]==0:L[i]=i*100
    elif L[i]<999:L[i]+=1000
    else:L[i]*=10
print(max(L))

#by sait2000
*_,a,b,c=sorted(input());print(['1'+b,c][a<b<c]+'000'[a<c:])
