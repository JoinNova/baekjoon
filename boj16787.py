#boj16787 マルバツスタンプ
n=int(input())
s=input()
chk=0;result=0
for i in range(n-1):
    if s[i]+s[i+1]=='OX' and chk==0:
        result+=1
        chk=1
    elif s[i]+s[i+1]=='XO' and chk==0:
        result+=1
        chk=1
    else:
        chk=0
print(result)


#02
input();s=input();f=s[0];k=r=0
for _ in s:r,k,f=[[r,0,_],[r+1,1,_]][f!=_ and k<1]
print(r)
