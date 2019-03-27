#boj16861 Harshad Numbers
t=input();n=sum(int(_)for _ in t)
while 1:
 if int(t)%n==0:print(t);break
 t=int(t)+1;n=sum(int(_)for _ in str(t))
