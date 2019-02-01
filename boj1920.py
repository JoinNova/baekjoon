###수 찾기

from sys import stdin
n=int(stdin.readline().strip())
nl=set(map(int,stdin.readline().split()))
m=int(stdin.readline().strip())
ml=list(map(int,stdin.readline().split()))
for _ in ml:
    print(len(nl.intersection({_})))

#02
i=input;i();l=set(i().split());i()
for _ in i().split():print(1 if _ in l  else 0)
