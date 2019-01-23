#1735 암호만들기
from itertools import*;import re
l,c=map(int,input().split());t=sorted([*input().split()]);p='aeiou'
for _ in list(combinations(t,l)):
    if len(re.sub(r'[aeiou]','',''.join(_)))>1 and len(re.sub(r'[aeiou]','',''.join(_)))<l:
        print(''.join(_))
#02
i=input;from itertools import*;import re;l,c=map(int,i().split());t=sorted([*i().split()])
for _ in list(combinations(t,l)):
 p=len(re.sub(r'[aeiou]','',''.join(_)))
 if p>1 and p<l:print(''.join(_))
 
#03
i=input;from itertools import*;import re;l=int(i()[:2]);t=sorted([*i()[::2]])
for _ in list(combinations(t,l)):
 r=''.join(_);p=len(re.sub(r'[aeiou]','',r))
 if l>p>1:print(r)
