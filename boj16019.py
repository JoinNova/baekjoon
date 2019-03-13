#boj16019 Are we there yet?
l=[*map(int,input().split())]
for i in range(5):
    f=e=0;r=[]
    front=l[:i][::-1]
    for _ in front:
        f+=_
        r.insert(0,f)
    r+=[0]
    end=l[i:]
    for _ in end:
        e+=_
        r+=[e]
    print(*r)
