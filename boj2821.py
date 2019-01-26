###컨베이어 벨트
###컨베이어 벨트
import sys;s=sys.stdin.readline;n,m=map(int,s().split());f=h=fl=[]
t=[int(s())for _ in'_'*n]
for i in range(m):
    f=int(s())
    for j in range(n):
        if len(fl)>=n:
            if fl[len(fl)-n]+t[j]*f<fl[len(fl)-n+j]:
                kk=fl[len(fl)-1]-fl[len(fl)-n]+t[j]*f
                for k in range(len(fl)):                 
                    fl[k]+=kk   
            fl.append(fl[len(fl)-n]+t[j]*f)
        elif i==0 and j==0:
            fl.append(t[j]*f)
        else:
            fl.append(fl[len(fl)-1]+t[j]*f)
print(fl[n-1])

