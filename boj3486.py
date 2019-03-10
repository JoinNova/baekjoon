#boj3486 Adding Reversed Numbers
for _ in'_'*int(input()):
    ans=''
    a,b=input().split()
    
    m=0
    if len(a)<len(b):
        a,b=b,a
    b=b+'0'*(len(a)-len(b))
    for i in range(len(a)):
        m=int(a[i])+int(b[i])+m
        if m>9:
            ans+=str(m%10)
            m=1
        else:
            ans+=str(m)
            m=0
    
    if m==1:
        ans+=str(m)
    print(int(ans))
    
#by cubelover
exec('print(int(str(sum(int(x[::-1]) for x in input().split()))[::-1]));'*int(input()))
