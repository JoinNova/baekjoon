#boj13718 tavan
import sys;s=sys.stdin.readline
n,m,k,x=map(int,s().split());x-=1;idx=[]
while x>=k:
    idx.append(x%k)
    x//=k
idx.append(x)
if len(idx)!=m:
    idx=idx+[0]*(m-len(idx))

word=s().strip()
for _ in'_'*m:
    sub=sorted(s().strip())
    word=word.replace('#',sub[idx.pop()],1)
    if idx==[]:break
print(word)
