#5073 삼각형과 세변
while 1:
 a,b,c=sorted(map(int,input().split()))
 if a==0:break
 if a+b<=c:print('Invalid')
 elif a==b==c:print('Equilateral')
 elif a==b or b==c:print('Isosceles')
 else:print('Scalene')
