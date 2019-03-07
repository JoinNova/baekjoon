#boj2754학점계산
p,x,n=[-.3,0,.3],'-0+',input();print('%.1f'%('FDCBA'.index(n[0])+p[x.index(n[1])])if n[0]!='F'else'0.0')

#by skygarlics
r=input()+'0';s=69-ord(r[0])+.3*('-0+'.find(r[1])-1);print(max(s,.0))

#by soyuz67
a=list(input()+'0')
print("%.1f"%max(0,(69-ord(a[0]))+[0,eval(a[1]+'0.3')][int(a[1]!='0')]))
