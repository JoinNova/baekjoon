#15953 상금 헌터
for i in'_'*int(input()):
 r=0;a,b=map(int,input().split())
 if a==0:pass
 elif a<2:r+=500
 elif a<4:r+=300
 elif a<7:r+=200
 elif a<11:r+=50
 elif a<16:r+=30
 elif a<22:r+=10
 if b==0:pass
 elif b<2:r+=512
 elif b<4:r+=256
 elif b<8:r+=128
 elif b<16:r+=64
 elif b<32:r+=32
 print(r*10**4)
