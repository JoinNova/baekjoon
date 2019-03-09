#boj2011 암호코드
import sys;s=sys.stdin.readline
code=s().strip();mod=1000000
if len(code)>1:
    if code[0]=='0':exit()
if code=='0' or code[0]=='0':print(0)
else:
    try:
        dp=[0 for _ in'_'*(len(code) + 1)]
        dp[0]=1
        dp[1]=1
        for i in range(2,len(code)+1):
            fir=int(code[i-2])
            sec=int(code[i-1])
            if fir >= 3 or fir== 0:
                if sec==0 and fir==0:print(0);exit()
                dp[i] = dp[i-1]
            else:
                if sec==0:
                    dp[i] = dp[i-2]
                else:
                    if fir==1:
                        dp[i]=dp[i-1]+dp[i-2]
                    elif fir== 2:
                        if sec> 6:
                            dp[i]=dp[i-1]
                        else:
                            dp[i]=dp[i-1]+dp[i-2]
        print(dp[len(code)]%mod)
    except:print(0)
    
#by sait2000
a=t=0;b=1
for c in map(int,input()):a,b,t=b,a*(9<t+c<27)+b*(c>0),c*10
print(b%10**6)

#by jaehunny
l=q=0;p=1
for i in input()[::-1]:k=int(i);l,q,p=k,p,k>0 and p+q*(k*10+l<27)
print(p%10**6)


#by jh05013
s = input()
ans = [0]*len(s)
if s[-1] != '0':
    ans[-1] = 1
if len(s)>1 and s[-2] != '0':
    ans[-2] = ans[-1]
    if int(s[-2:]) <= 26:
        ans[-2]+= 1
for i in range(len(s)-3, -1, -1):
    if s[i] != '0':
        ans[i] = ans[i+1]
        if int(s[i:i+2]) <= 26:
            ans[i]+= ans[i+2]
    ans[i]%= 1000000
print(ans[0])
