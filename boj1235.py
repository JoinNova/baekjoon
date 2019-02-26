#boj1235 학생번호
l=[];n=int(input())
for _ in'a'*n:
    t=input()
    l.append(t)
idx=len(l[0])-1
while 1:
    s=set()
    for _ in l:
        s.add(_[idx:])
    if len(s)==n:
        break
    #print(s)
    idx-=1
print(len(l[0])-idx)
