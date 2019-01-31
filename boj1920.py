###수 찾기
from sys import stdin
n=int(stdin.readline().strip())
nl=set(map(int,stdin.readline().split()))
m=int(stdin.readline().strip())
ml=list(map(int,stdin.readline().split()))
for _ in ml:
    print(len(nl.intersection({_})))
