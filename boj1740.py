#1740 거듭제곱
n=int(input());a=b=0
while n:
 if n%2:a+=3**b
 n//=2;b+=1
print(a)
