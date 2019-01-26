#13015 별찍기-23
n=int(input());p='*';b=' '
for i in range(n-1):
    if i==0:
        print(p*n+b*(2*n-3)+p*n)
    else:
        print(b*i+p+b*(n-2)+p+b*(2*(n-i)-3)+p+b*(n-2)+p)
print(b*(n-1)+p+b*(n-2)+p+b*(n-2)+p)
for i in range(n-2,-1,-1):
    if i==0:
        print(p*n+b*(2*n-3)+p*n)
    else:
        print(b*i+p+b*(n-2)+p+b*(2*(n-i)-3)+p+b*(n-2)+p)
#02
n=int(input());p='*';b=' ';r=[]
for i in range(n-1):r+=[p*n+b*(2*n-3)+p*n if i==0 else b*i+p+b*(n-2)+p+b*(2*(n-i)-3)+p+b*(n-2)+p]
print(*r,b*(n-1)+p+b*(n-2)+p+b*(n-2)+p,*r[::-1],sep='\n')
#03
n=int(input());k=n-2;p='*';b=' ';r=[p*n+b*(2*k+1)+p*n]
for i in range(1,n-1):r+=[b*i+p+b*k+p+b*(2*(k-i)+1)+p+b*k+p]
print(*r,b*(n-1)+p+b*k+p+b*k+p,*r[::-1],sep='\n')
