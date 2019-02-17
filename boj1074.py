#boj1074 Z

def z(n,r,c,s,result):
 if r<2 and c<2:
  result+=(r*2+c)
  return result
 s//=2;i,j=r//s,c//s
 result+=(i*2+j)*s**2
 r-=i*s;c-=j*s
 return z(n,r,c,s,result)

n,r,c=map(int,input().split());result=0;s=2**n
print(z(n,r,c,s,result))
