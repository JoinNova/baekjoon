#1011 Fly me to the Alpha Centauri
for i in range(int(input())):
    x,y=input().split()
    n=int(y)-int(x)
    a=0
    chk=0
    for i in range(n):
        chk+=1
        a+=int(i/2)+1
        if a>=n:
            break
    print(chk)
#02
exec('n=-eval(input().replace(" ","-"));a=k=0\nfor i in range(n):\n k+=1;a+=int(i/2)+1\n if a>=n:break\nprint(k)\n'*int(input()))
