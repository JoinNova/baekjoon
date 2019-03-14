#boj16505 별
def byulmake(form,seq):
    global byul,blank
    line='';j=0;new=[]
    for _ in form:
        line=_+blank*j+_
        j+=1
        new+=[line]
    for _ in form:
        line=_
        new+=[line]
    return new

n=int(input())
byul='*';blank=' ';result=['*']
for i in range(n):
    result=byulmake(result,i)
print(*result,sep='\n')
