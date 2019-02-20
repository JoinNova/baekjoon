n=int(input());t=input();result=0
for i in range(n-1):
    c=input();chk=0
    if len(t)==len(c):
        x,y=sorted(t),sorted(c)
        if x==y:
            result+=1
        else:
            for _ in x:
                try:
                    y.remove(_)
                    #print(y)
                except:chk+=1
            if chk==1:result+=1
        
    if len(t)-len(c)==1:
        compare=sorted(t)
        for _ in c:
            try:
                compare.remove(_)
                #print(compare)
            except:chk=1
        if chk==0:result+=1
    if len(c)-len(t)==1:
        compare=sorted(c)
        for _ in t:
            try:
                compare.remove(_)
                #print(compare)
            except:chk=1
        if chk==0:result+=1

print(result)
