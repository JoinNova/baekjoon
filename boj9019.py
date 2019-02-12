#boj9019 DSLR
'''
def D(soo):
#    subD=str((2*int(soo))%10000)
    #subD=(4-len(subD))*'0'+subD
#    return (4-len(subD))*'0'+subD

    #subD=(2*soo)%10000
    #subD=(4-len(subD))*'0'+subD
    return (2*soo)%10000

def S(soo):
#    subS=str((10000+int(soo)-1)%10000)
    #subS=(4-len(subS))*'0'+subS
#    return (4-len(subS))*'0'+subS

    #subS=str((10000+soo-1)%10000)
    #subS=(4-len(subS))*'0'+subS
    return (10000+soo-1)%10000

def L(soo):
    soo=str(soo)
    if len(soo)<4:
        subL=(4-len(soo))*'0'+soo
        return int(subL[1:]+subL[0])
    #pivot=subL[0]
    #subL=subL[1:]+pivot
    return int(soo[1:]+soo[0])

def R(soo):
    soo=str(soo)
    if len(soo)<4:
        subR=(4-len(soo))*'0'+soo
        return int(subR[-1]+subR[:3])
    #pivot=subR[-1]
    #subR=pivot+subR[:3]
    return int(soo[-1]+soo[:3])

def dfs(x,y):
    tree=[x];result=[''];front=0;end=1#;result.add('_');print(list(result)[0]);
    while 1:
        chk=0
        for i in range(front,end):
            #print(list(result)[i])
            soo1,make1=tree[i],result[i]
            sooD=(2*soo1)%10000
            if sooD==y:
                #makeD=make1+'D'
                return print(make1+'D')
            elif tree.count(sooD)==0:
                tree.append(sooD);makeD=make1+'D';result.append(makeD);chk+=1
            sooS=(10000+soo1-1)%10000
            if sooS==y:
                #makeS=make1+'S'
                return print(make1+'S')
            elif tree.count(sooS)==0:
                tree.append(sooS);makeS=make1+'S';result.append(makeS);chk+=1
            sooL=L(soo1)   
            if sooL==y:
                #makeL=make1+'L'
                return print(make1+'L')
            elif tree.count(sooL)==0:
                tree.append(sooL);makeL=make1+'L';result.append(makeL);chk+=1
            sooR=R(soo1)     
            if sooR==y:
                #makeR=make1+'R'
                return print(make1+'R')
            elif tree.count(sooR)==0:
                tree.append(sooR);makeR=make1+'R';result.append(makeR);chk+=1

            
        front,end=end,end+chk
        #if len(tree)==10000:return result
import time
import sys;put=sys.stdin.readline
for _ in'_'*int(put()):
    start=time.time()
    a,b=map(int,put().split())
    #a=(4-len(a))*'0'+a
    #b=(4-len(b))*'0'+b
    dfs(a,b)
    print(time.time()-start)
'''

def L(soo):
    soo=str(soo)
    if len(soo)<4:
        subL=(4-len(soo))*'0'+soo
        return int(subL[1:]+subL[0])
    #pivot=subL[0]
    #subL=subL[1:]+pivot
    return int(soo[1:]+soo[0])
lis=[]
for i in range(0,10000):
    lis+=[L(i)]
print(lis)
