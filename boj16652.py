#boj16652 Email Destruction
import sys;s=sys.stdin.readline
import re
recnt=0;box=[];cnt=[]
n,k=map(int,input().split())
for _ in'_'*k:
	txt=s().strip()
	mail=re.sub('Re: ','',txt)
	recnt=txt.count('Re: ')+1
	if mail in box:
		idx=box.index(mail)
		cnt[idx]=max(recnt,cnt[idx])
	else:
		box.append(mail)
		cnt.append(recnt)
print('YNEOS'[sum(cnt)>n::2])
#print(*box,*cnt)
