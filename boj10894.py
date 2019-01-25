#10984 내학점을 구해줘
for i in 'a'*int(input()):
 t,a=0,0
 for i in 'a'*int(input()):
   c,s=map(float,input().split())
   t+=c
   a+=c*s
 k=str(a/t).split('.')
 if len(k[1])==1:
  k=float(k[0]+'.'+k[1][0]) 
 elif int(k[1][1])>=5:
  if str(int(k[1][0])+1)=='10':
   k=float(str(int(k[0])+1)+'.'+'0')
  else:k=float(k[0]+'.'+str(int(k[1][0])+1))
 else:
  k=float(k[0]+'.'+k[1][0])  
 print('%d %.1f'%(t,k))

#02소수오류로안됨
#exec('t,a=0,0;exec("c,s=map(float,input().split());t+=c;a+=c*s;"*int(input()));print("%d %.1f"%(t,a/t));'*int(input()))
