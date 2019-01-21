#14726 신욘카드판별
for i in range(int(input())):
    t=input()
    #print(t[::2]) #짝수
    #print(t[::-1][::2])#홀수
    r=[int(_)*2 for _ in t[::2]]
    #print(r)
    r=[eval(str(int(_)*2)[0]+'+'+str(int(_)*2)[1])if int(_)*2>=10 else int(_)*2 for _ in t[::2]]
    #print(r)
    #print(t[::-1][::2])
    c=sum(int(_)for _ in t[::-1][::2])+sum(int(_)for _ in r)
    if c/10==c//10:print('T')
    else:print('F')

#02
for i in range(int(input())):
    t=input()
    r=[eval(str(int(_)*2)[0]+'+'+str(int(_)*2)[1])if int(_)*2>9 else int(_)*2 for _ in t[::2]]
    c=sum(int(_)for _ in t[::-1][::2])+sum(int(_)for _ in r)
    if c/10==c//10:print('T')
    else:print('F')

#03
i=input;n=int;exec('t=i();r=[eval(str(n(_)*2)[0]+"+"+str(n(_)*2)[1])if n(_)*2>9 else n(_)*2 for _ in t[::2]];c=sum(n(_)for _ in t[::-1][::2])+sum(n(_)for _ in r);print("T"if c/10==c//10else"F");'*n(i()))

#04
i=input;n=int
for _ in'a'*(n(i())):r=j=0;t=i();exec('if j%2==0:\n c=n(t[j])*2\n r+=n(str(c)[1])+1 if c>9 else c\nelse:r+=n(t[j])\nj+=1\n'*len(t));print('T'if r//10==r/10else'F')
