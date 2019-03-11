#boj1837 암호제작

import sys;s=sys.stdin.readline
p=s().strip().split()
max=1000000
A=[True]*max;pn=[2]
for i in range(3,max+1,2):
	if not A[i]: continue
	pn.append(i)
	for e in range(i*i,max+1,i*2):
		A[e]=False

result='GOOD'
for _ in pn:
    if _>int(p[1]):break
    if int(p[0])%_==0:
        if int(p[1])==_:
            break
        else:
            result='BAD '+str(_)
            break

print(result)

#by holenet
p,k=map(int,input().split())
for r in range(2,k):
 if p%r==0:print('BAD',r);break
else:print('GOOD')
