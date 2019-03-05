#boj16786 すごろくと駒
n=int(input())
l=[*map(int,input().split())]
m=int(input())
command=[*map(int,input().split())]
for _ in command:
    if l[_-1]+1<=2019 and not l[_-1]+1 in l:
        l[_-1]+=1
print(*l,sep='\n')

#02
i=input;f=lambda:map(int,input().split());n=int(i());l=[*f()];m=int(i())
for _ in[*f()]:
 if l[_-1]<2019 and not l[_-1]+1 in l:l[_-1]+=1
print(*l,sep='\n')
