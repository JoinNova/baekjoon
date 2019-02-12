#by iknoom1107
n=input()
N=len(n)

dp=[[False]*N for _ in range(N)]
for i in range(N):dp[i][i]=True
for i in range(N-1):
	if n[i]==n[i+1]:dp[i][i+1]=True
	else:dp[i][i+1]=False

for k in range(2,N+1):
	for i in range(N-k):
		j=i+k
		if dp[i+1][j-1] and n[i]==n[j]:dp[i][j]=True
		else:dp[i][j]=False

dp2=[0]*N
dp2[0]=1
for i in range(1,N):
	dp2[i]=dp2[i-1]+1
	for j in range(i-1):
		if n[j]==n[i] and dp[j+1][i-1]:
			if j==0:dp2[i]=1
			else:dp2[i]=min(dp2[i],dp2[j-1]+1)
	if n[i-1]==n[i]:
		if i==1:dp2[i]=1
		else:dp2[i]=min(dp2[i],dp2[i-2]+1)

print(dp2[-1])

#by cubelover
s=' '.join(input())+' '
n=len(s)
d=[2222]*(n+1)
d[0]=0
for i in range(n):
	j=0
	while i-j>=0 and i+j<n and s[i-j]==s[i+j]:
		d[i+j+1]=min(d[i+j+1],d[i-j]+1)
		j+=1
print(min(d[n-1],d[n]))


#by jh05013
d = input()
n = len(d)
palin = [[None]*n for i in range(n)]
minsp = [2500]*(n+1)
# palin[i][j] == True iff d[i:j+1] is palindrome or i>j
# minsp[i] == minimum split of d[:i]

def get(L,y,x):
    if 0<=y<len(L) and 0<=x<len(L[0]): return L[y][x]
    return 1

for j in range(n):
    for i in range(n):
        if i>=j: palin[i][j] = True
        elif d[i]==d[j] and get(palin,i+1,j-1): palin[i][j] = True
        else: palin[i][j] = False

minsp[0] = 0
for i in range(1,n+1):
    for j in range(i):
        if palin[j][i-1]:
            minsp[i] = min(minsp[i], minsp[j]+1)
print(minsp[-1])
