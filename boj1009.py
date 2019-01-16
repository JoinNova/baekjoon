#1009 분산처리
from sys import stdin
for i in range(int(stdin.readline().strip())):
    a,b=map(str,stdin.readline().split())
    aa=a[len(a)-1:]
    if aa=='1':
        print(1)
    elif aa=='2':
        l=[2,4,8,6]
        if int(b)%4-1==-1:
            print(l[3])
        else:
            print(l[int(b)%4-1])
    elif aa=='3':
        l=[3,9,7,1]
        if int(b)%4-1==-1:
            print(l[3])
        else: 
            print(l[int(b)%4-1])
    elif aa=='4':
        l=[4,6]
        if int(b)%2-1==-1:
            print(l[1])
        else:
            print(l[int(b)%2-1])
    elif aa=='5':
        print(5)
    elif aa=='6':
        print(6)
    elif aa=='7':
        l=[7,9,3,1]
        if int(b)%4-1==-1:
            print(l[3])
        else:
            print(l[int(b)%4-1])
    elif aa=='8':
        l=[8,4,2,6]
        if int(b)%4-1==-1:
            print(l[3])
        else:
            print(l[int(b)%4-1])
    elif aa=='9':
        l=[9,1]
        if int(b)%2-1==-1:
            print(l[1])
        else:
            print(l[int(b)%2-1])
    else :
        print(10)
