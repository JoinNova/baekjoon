#5613 계산기 프로그램
a=int(input())
while 1:
    b=input()
    if b=='=':
        print(a)
        break
    c=int(input())
    if b=='+':
        a+=c
    elif b=='-':
        a-=c
    elif b=='*':
        a*=c
    elif b=='/':
        a//=c
