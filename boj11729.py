#boj11729 하노이 탑 이동 순서
def hanoi(n,beg,aux,end,l):
    if n==1:
        l.append([beg,end])
    else:
        hanoi(n-1,beg,end,aux,l)
        hanoi(1,beg,aux,end,l)
        hanoi(n-1,aux,beg,end,l)
n=int(input());l=[]
hanoi(n,1,2,3,l)
print(len(l))
for _ in l:
    print(*_)
