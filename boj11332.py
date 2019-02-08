#boj11332
#import time
import math;i=int;c=i(input());r=10**8
#start=time.time()
for _ in range(c):
    s=[*map(str,input().split())]
    s,N,t,l=s[0][2:-1].replace('^','**'),i(s[1]),i(s[2]),i(s[3])
    #print(s,N,t,l)
    '''
    try:
        #print(eval(s))
        eval(s)
    except:
        s='math.factorial('+s[:-1]+')'
        #print(eval(s))
    '''
    if s[-1]=='!':s='math.factorial('+s[:-1]+')'
    try:
        if eval(s)/l>r/t:print("TLE!")
        #if eval(s)*t>r*l:print("TLE!")
        else:print("May Pass.")
    except:
        print("TLE!")
'''
        s='math.factorial('+s[:-1]+')'
        #print(eval(s))
    #k=eval(s)
    if eval(s)/l>r/t:print("TLE!")
    else:print("May Pass.")
'''
#print(time.time()-start)

#02

import math;i=int;c=i(input());r=10**8
for _ in range(c):
    s=[*map(str,input().split())]
    s,N,t,l=s[0][2:-1].replace('^','**'),i(s[1]),i(s[2]),i(s[3])
    if s[-1]=='!':s='math.factorial('+s[:-1]+')'
    try:
        if eval(s)/l>r/t:print("TLE!")
        else:print("May Pass.")
    except:
        print("TLE!")

#03
import math;i=int;I=input;p=print;T='TLE!';r=10**8
for _ in'_'*i(I()):
 s=[*map(str,I().split())];s,N,t,l=s[0][2:-1].replace('^','**'),i(s[1]),i(s[2]),i(s[3])
 if s[-1]=='!':s='math.factorial('+s[:-1]+')'
 try:p(T if eval(s)/l>r/t else"May Pass.")
 except:p(T)

#by veydpz
import re
INF = 10**10
def fac(x):
	ret = 1
	for i in range(1,x+1):
		ret *= i
	return ret
def fac(n):
	ret = 1
	for i in range(1,n+1):
		ret *= i
	return ret
for _ in range(int(input())):
	s, *_ = input().split()
	N, t, l = map(int, _)
	s = re.findall(r'O\((.*)\)', s)[0]
	s = s.replace('^','**')
	if(s == 'N!'):
		if(N > 20):
			x = INF
		else:
			x = fac(N)
	elif(s == '2**N'):
		if(N > 40):
			x = INF
		else:
			x = 2**N
	else:
		x = eval(s)
	print('TLE!' if x*t > l*(10**8) else 'May Pass.')
