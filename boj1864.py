#1864 문어숫자
t=input()
while t!='#':
 r=0;k=len(t)-1
 for _ in t:r+=('/-\(@?>&%'.index(_)-1)*8**k;k-=1
 print(r);t=input()

#02
while 1:
 r=0;t=input();k=len(t)-1
 if t=='#':break
 for _ in t:r+=('/-\(@?>&%'.index(_)-1)*8**k;k-=1
 print(r)
#03
p='/-\(@?>&%'
while 1:
 r=0;t=input();k=len(t)-1
 if t=='#':break
 for _ in t:r+=(p.index(_)-1)*8**k;k-=1
 print(r)
