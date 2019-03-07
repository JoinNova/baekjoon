#boj13300 방배정
room=[[False,False]for _ in'_'*6];result=0
n,k=map(int,input().split())
for _ in'_'*n:
    s,y=map(int,input().split())
    room[y-1][s]+=1
for _ in room:
    for __ in _:
        result+=[__//k+1,__//k][__%k<1]
print(result)


#02
f=lambda:map(int,input().split());m=[[0,0]for _ in'_'*6];r=0;n,k=f();exec('s,y=f();m[y-1][s]+=1;'*n)
for _ in m:
 for __ in _:r+=[__//k+1,__//k][__%k<1]
print(r)

#03
f=lambda:map(int,input().split());m=[[0,0]for _ in'_'*6];r=j=0;n,k=f();exec('s,y=f();m[y-1][s]+=1;'*n);exec("a,b=m[j][0],m[j][1];exec('r+=[a//k+1,a//k][a%k<1];a=b;'*2);j+=1;"*6);print(r)
