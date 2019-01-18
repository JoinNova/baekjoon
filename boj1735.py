#1735 분수 합
from fractions import Fraction as f;i=input;a,b=map(int,i().split());c,d=map(int,i().split());r=str(f(a*d+c*b,b*d));print(r.replace('/',' ') if r.count('/')==1 else r.replace('/',' ')+' 1')

#02
from fractions import Fraction as f;i=input;a,b=map(int,i().split());c,d=map(int,i().split());r=str(f(a,b)+f(c,d));print(r+' 1' if r.count('/')==0 else r.replace('/',' '))

#03
i=input;import math;a,b=map(int,i().split());c,d=map(int,i().split());a,b=a*d+b*c,b*d;g=math.gcd(a,b);print(a//g,b//g)

