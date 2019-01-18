#2437 저울
i=input;i();r=1
for _ in sorted(map(int,i().split())):
 if _>r:break
 r+=_
print(r)
#02아직이해안가감.by sait2000
I=input;f=r=1;I()
for a in sorted(map(int,I().split())):f&=a<=r;r+=f*a
print(r)
