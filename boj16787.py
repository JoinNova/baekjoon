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
