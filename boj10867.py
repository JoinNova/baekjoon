#10867 중복뺴고 정렬하기

import sys;s=sys.stdin.readline;l=[];
for _ in map(int,s().split()):
 if _ not in l:l.append(_)
print(*sorted(l))

#input();print(*sorted(set(map(int,input().split()))))
#input();print(*sorted({*input().split()},key=int))

