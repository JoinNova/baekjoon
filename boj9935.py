#boj9935 문자열폭발
t=[*input()];c=[*input()][::-1];l=len(c);r=[]
while len(t)>0:
 r+=[t.pop()]
 if r[-l:]==c:r=r[:len(r)-l]
print(''.join(r[::-1])if len(r)>0else'FRULA')
print(*r[::-1] if len(r)>0else'FRULA',sep='')

#02
t=[*input()];c=[*input()][::-1];l=len(c);r=[]
while len(t)!=0:
 r+=[t.pop()]
 if r[-l:]==c:[r.pop()for _ in'a'*l]
print(*r[::-1]or'FRULA',sep='')

#03
t=input();c=[*input()];l=len(c);r=[]
for _ in t:
 r+=[_]
 if r[-l:]==c:r[-l:]=[]
print(''.join(r)or"FRULA")

#by sait2000
s,p,*r=input(),[*input()];q=len(p)
for c in s:
 r+=c
 if r[-q:]==p:r[-q:]=()
print(''.join(r)or'FRULA')
