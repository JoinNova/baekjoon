#boj8979 올림픽
n,k=map(int,input().split());l=[]
for i in range(n):
 a=list(map(int,input().split()))
 if a[0]==k:k=a[1:]
 l.append(a[1:])
l.sort(reverse=True);print(l.index(k)+1)

#02
i=input;n,k=map(int,i().split());l=[]
for _ in'a'*n:
 a=[*map(int,i().split())]
 if a[0]==k:k=a[1:]
 l+=[a[1:]]
l.sort(reverse=True);print(l.index(k)+1)

#03
i=input;n,k=map(int,i().split());l=[];exec('a=[*map(int,i().split())]\nif a[0]==k:k=a[1:]\nl+=[a[1:]];'*n);l.sort(reverse=True);print(l.index(k)+1)
