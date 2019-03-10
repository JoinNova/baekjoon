#boj16428 A/B-3
a,b=map(int,input().split())
if b>0:
    k=a//b
    print(k)
    j=a%abs(b)
    print(j)
else:
    k=abs(a//abs(b))
    j=a%abs(b)

    if a>0:
        print(-k)
        print(j)
    else:
        print(k)
        print(j)

#by cubelover
a,b=map(int,input().split());print(a//b if b>0 else-(a//-b));print(a%abs(b))

#by milkclouds
a,b=map(int,input().split())
c,d=divmod(a,b)
if a!=0 and b<0:
	c,d=c+1,d-b
print(c)
print(d)

#by portableangel
a, b = map(lambda x:int(x), input().split(' '))

rem = a % b
if rem < 0:
	rem -= b

print((a-rem)//b)
print(rem)
