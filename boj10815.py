#10815 숫자카드
input();l=set(map(str,input().split()));a=len(l);input()
for _ in input().split():l.add(_);print('1' if a==len(l) else '0',end=' ');a=len(l)

#02
l={};input();r=''
for _ in input().split():l[_]='1 '
input()
for _ in input().split():
 try:r+=l[_]
 except:r+='0 '
print(r[:-1])

#03
input()
s = set(input().split())
input()
print(' '.join(map(lambda t: '1' if t in s else '0', input().split())))

#04 이해못한코드
i=input;i();d={*i().split()};i();print(*(+(v in d)for v in i().split()))

'''
#채점번호 10694761 출력형식 이상 백준 버그임.
a=dict()
input()
for x in input().split():
    a[x]=1
input()
for x in input().split():
    if x in a:
        print(a[x])
    else: print(0)

'''
