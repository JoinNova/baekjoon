#boj10799 쇠막대기
import sys;t=sys.stdin.readline();l=[];r=0
for i in range(len(t)):
 if t[i]=="(":l+=[i]
 elif t[i]==")":
  if i-l[-1]==1:r+=len(l)-1
  else:r+=1
  l.pop()
print(r)

#02
t=input();l=[];r=0
for i in range(len(t)):
 if t[i]=="(":l+=[i]
 elif t[i]==")":
  if i-l[-1]==1:r+=len(l)-1
  else:r+=1
  l.pop()
print(r)

#by justin0225
s=input()
s=s.replace('()','L')
num=s.count('(')
c=0
for i in s:
	if i=='(':
		c+=1
	elif i==')':
		c-=1
	elif i=='L':
		num+=c

print(num)

#by sait2000
r=d=i=0
for c in input():j=')'>c;d+=j+j-1;r+=(j or d)*i;i=j
print(r)

#by milkclouds
import sys
st=0;t=0;ret=0
for i in sys.stdin.readline().rstrip():
	if i=='(':
		st+=1;t=1
	else:
		st-=1
		if t:ret+=st
		else:ret+=1
		t=0
print(ret)
