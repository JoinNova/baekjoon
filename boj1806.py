#boj1806 부분합
import sys;s=sys.stdin.readline
    
n,target=map(int,s().split())
lis=list(map(int,input().split()))
start=0;end=0;hap=0;result=n+1
while start <= end:
    try:
        if hap < target and end < n:
            hap+=lis[end];end+=1
        else:
            hap-=lis[start];start+=1
        if hap>=target:
            result=min(result,end-start)
    except:break
if result > n:
    result=0
            
print(result)
#print(result)


#boj1806 부분합
f=lambda:map(int,input().split());n,t=f();l=[*f()];s=0;e=0;h=0;r=n+1
while 1:
 try:
  if h < t and e < n:h+=l[e];e+=1
  else:h-=l[s];s+=1
  if h>=t:r=min(r,e-s)
 except:break
if r>n:r=0
print(r)
#print(result)

#by sait2000
[n,S],[*a]=eval('map(int,input().split()),'*2);r=9**9;
z=0;i=j=0
while i+j<2*n:
 if z<S and j<n:z+=a[j];j+=1
 else:z-=a[i];i+=1
 if z>=S:r=min(r,j-i)
print(r%9**9)
