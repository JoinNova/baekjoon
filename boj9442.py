#boj9422 sort me
a=1
while 1:
    n=input();l=[]
    if n=='0':break
    n=n.split();p=n[1]
    for i in range(int(n[0])):l+=[input()]
    for i in range(len(l)-1):
        for k in range(len(l)-1):
            x,y=l[k],l[k+1];c=min(len(x),len(y))
            for j in range(c):
                if p.index(x[j])>p.index(y[j]):
                    l[k],l[k+1]=l[k+1],l[k]
                    break
                elif p.index(x[j])<p.index(y[j]):
                    break
                elif j==c-1:
                    if len(x)>len(y):
                        l[k],l[k+1]=l[k+1],l[k]
    
    print('year '+str(a),*l,sep='\n');a+=1

#02
a=1
while 1:
 n=input();l=[]
 if n=='0':break
 n=n.split();n,p=int(n[0]),n[1];l=[input()for i in'_'*n]
 for i in range(n-1):
  for k in range(n-1):
   x,y=l[k],l[k+1];c=min(len(x),len(y))
   for j in range(c):
    if p.index(x[j])>p.index(y[j]):l[k],l[k+1]=l[k+1],l[k];break
    elif p.index(x[j])<p.index(y[j]):break
    elif j==c-1 and len(x)>len(y):l[k],l[k+1]=l[k+1],l[k]
 print('year %d'%a,*l,sep='\n');a+=1
