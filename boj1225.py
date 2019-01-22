#1225 이상한 곱셈

a,b=map(str,input().split())
a=sum(int(_) for _ in a)
print(sum(a*int(_) for _ in b))

#02 pypy3
a,b=map(str,input().split());print(sum(sum(int(_) for _ in a)*int(_) for _ in b))

#03
a,b=input().split()
print(sum(int(_)for _ in a)*sum(int(_)for _ in b))

#04
a,b=input().split();print(sum(map(int,a))*sum(map(int,b)))

#05 by YunGoon
a,b=map(eval,map('+'.join,input().split()));print(a*b)
