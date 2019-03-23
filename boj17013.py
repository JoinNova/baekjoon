#boj17013 Flipper
import sys;s=sys.stdin.readline
r='1 23 4'
t=s().strip()
r=[r,'3 41 2'][t.count('H')%2]
r=[r,r[2]+' '+r[0]+r[5]+' '+r[3]][t.count('V')%2]
print(r[:3]+'\n'+r[3:])

#02
r='1 23 4';t=input();r=[r,'3 41 2'][t.count('H')%2];r=[r,r[2]+' '+r[0]+r[5]+' '+r[3]][t.count('V')%2];print(r[:3]+'\n'+r[3:])
