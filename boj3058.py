#boj3058 짝수를 찾아라
for i in'i'*int(input()):
 h=[]
 for _ in[*map(int,input().split())]:
  if _%2==0:
   h+=[_]
 print(sum(h),sorted(h)[0])
 
#02
exec('h=[ _ for _ in[*map(int,input().split())]if _%2<1];print(sum(h),min(h));'*int(input()))
