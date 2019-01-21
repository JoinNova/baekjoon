#15668 방 번호
r='-1';n=int(input())
for i in range(1,n//2):
 if n<987654322 and (len(str(n))+len(str(i)))<11:
  a=str(n-i);b=str(i)
  if len(set(a+b))==len(a+b):r=a+' + '+b;break
 else:break
print(r)

r=-1;n=int(input());s=str;
for i in range(1,n//2+1):
 if len(s(n))+len(s(i))<11:
  a=s(n-i);b=s(i);c=set(a+b)
  if len(c)==len(a+b):r=a+' + '+b;break
 else:break
print(r)
