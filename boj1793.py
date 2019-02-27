#boj1793 타일링

while 1:
    try:
        a=b=1
        for i in range(int(input())):
            a,b=b,a*2+b
        print(a)
    except: break  

#02
while 1:
 try:a=b=1;exec('a,b=b,a*2+b;'*int(input()));print(a)
 except:break
