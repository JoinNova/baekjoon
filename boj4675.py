'''
import sys;s=sys.stdin.readline
f=[]
while 1:
	t=s().strip()
	if t=='X'*6:break
	f+=[t]
f.sort()
while 1:
	t=s().strip();chk=0
	if t=='X'*6:break
	for _ in f:
		if len(_)==len(t) and sorted(set(_))==sorted(set(t)):
				print(_)
				chk=1
	if chk==0:print('NOT A VALID WORD')
	print('*'*6)
'''
p='abcdefghijklmnopqrstuvwxyz'
a=[0]*26;b=[0]*26
f=[]
while 1:
 t=input()
 if t=='XXXXXX':break
 f+=[t]
f.sort()
while 1:
 t=input();chk=0
 if t=='XXXXXX':break
 for _ in f:
  a=[0]*26;b=[0]*26
  if _!=t and len(_)==len(t):
   #print(_,t)
   for i in range(len(_)):
    a[p.index(_[i])]+=1
    b[p.index(t[i])]+=1
   #print(a,b,sep='\n')
   if a==b:print(_);chk=1
 if chk==0:print('NOT A VALID WORD')
 print('******')
