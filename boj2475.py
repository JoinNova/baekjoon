#2475 검증수
r=0
for _ in input().split():r+=int(_)**2
print(r%10)
#02
print(sum(_**2 for _ in map(int,input().split()))%10)
#03
print(sum(int(_)**2for _ in input().split())%10)


