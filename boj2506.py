#2506 점수계산
i=input;i();d=r=0
for _ in i()[::2]:
 if _=='1':r+=1+d;d+=1
 else:d=0
print(r)

#02
i=input;i();d=r=0
for _ in i()[::2]:d=(d+1)*int(_);r+=d
print(r)
