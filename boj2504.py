###괄호의 값
from sys import stdin
from re import sub
from re import match
t = stdin.readline().strip()
chka=0
chkb=0
if len(t)%2==0:
    if t.count('[')==t.count(']') and t.count('(')==t.count(')'):    
        t=sub(r'[\]]{1}[\[]{1}',']+[',t)
        t=sub(r'[\]]{1}[(]{1}',']+(',t)
        t=sub(r'[)]{1}[\[]{1}',')+[',t)
        t=sub(r'[)]{1}[(]{1}',')+(',t)
        t=sub(r'[\[]{1}[\]]{1}','3',t)
        t=sub(r'[(]{1}[)]{1}','2',t)
        t=sub(r'[(]{1}[2][)]{1}','2*2',t)
        t=sub(r'[(]{1}[3][)]{1}','2*3',t)
        t=sub(r'[\[]{1}[2][\]]{1}','2*3',t)
        t=sub(r'[\[]{1}[3][\]]{1}','3*3',t)
        new=str()
        for _ in t:
            if _=='(':
                new+='2*('
                chka+=1
            else:
                new+=_
        t=new
        new=str()
        for _ in t:
            if _=='[':
                new+='3*('
                chkb+=1
            else:
                if _==']':
                    new+=')'
                else:
                    new+=_
        try:
            if eval(new)!=():
                print(eval(new))
            else:
                print(0)
        except:
            print(0)
    else:
        print(0)
else:
    print(0)
