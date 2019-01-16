#1002터렛
for _ in 'i'*int(input()):
 a,b,c,x,y,z=map(int,input().split());d=(a-x)**2+(b-y)**2
 if c==z:
  if d>(2*c)**2:print(0)
  elif d==(2*c)**2:print(1)
  elif d==0:print(-1)
  else:print(2)
 else:
  if d>(c+z)**2:print(0)
  elif d==(c+z)**2:print(1)
  elif d>(c-z)**2:print(2)
  elif d==(c-z)**2:print(1)
  else:print(0)
#02
f=lambda x:print(x);exec('a,b,c,x,y,z=map(int,input().split());d=(a-x)**2+(b-y)**2\nif c==z:\n if d>(2*c)**2:f(0)\n elif d==(2*c)**2:f(1)\n elif d==0:f(-1)\n else:f(2)\nelse:\n if d>(c+z)**2:f(0)\n elif d==(c+z)**2:f(1)\n elif d>(c-z)**2:f(2)\n elif d==(c-z)**2:f(1)\n else:f(0)\n'*int(input()))
