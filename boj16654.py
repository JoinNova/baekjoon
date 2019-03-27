#boj16654 Generalized German Quotation
import sys;s=sys.stdin.readline
def pri(txt,r,l):
    #print(txt.count('<'),txt.count('>'))
    try:
        if txt[0]=='>':
            for i in range(0,len(txt),2):
                if txt[i]=='>':
                    print('[',end='')
                    r-=1
                else:
                    print(']',end='')
                    l-=1
                if r==l:
                    #print(txt[i+2:])
                    return pri(txt[i+2:],r,l)

        else:
            for i in range(0,len(txt),2):
                if txt[i]=='<':
                    print('[',end='')
                    r-=1
                else:
                    print(']',end='')
                    l-=1
                if r==l:
                    return pri(txt[i+2:],r,l)
    except:sys.exit()
    
string=s().strip()
if string.count('<')!=string.count('>'):
    print('Keine Loesung')
else:
    pri(string,string.count('<'),string.count('>'))
    
#02
