#1213 팰린드롬만들기

p='ABCDEFGHIJKLMNOPQRSTUVWXYZ';l=[0]*26;k=0;t=c=''
for _ in input():l[p.index(_)]+=1
for _ in range(26):
 if l[_]%2!=0:k+=1;c=p[_]
 t+=p[_]*(l[_]//2)
print("I'm Sorry Hansoo"if k>1 else t+c+t[::-1])

#02
p='ABCDEFGHIJKLMNOPQRSTUVWXYZ';l=[0]*26;k=_=0;t=c=''
for i in input():l[p.index(i)]+=1
exec('if l[_]%2!=0:k+=1;c=p[_]\nt+=p[_]*(l[_]//2);_+=1\n'*26)
print("I'm Sorry Hansoo"if k>1 else t+c+t[::-1])

#03
l=[0]*91;k=_=0;t=c=''
for i in input():l[ord(i)]+=1
exec('if l[_]%2!=0:k+=1;c=chr(_)\nt+=chr(_)*(l[_]//2);_+=1\n'*91);print("I'm Sorry Hansoo"if k>1else t+c+t[::-1])
