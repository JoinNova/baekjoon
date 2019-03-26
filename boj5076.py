#boj5076 web pages
line=input()
while'#'!=line:
    try:
        TF=0;head='';flag=0;slash=0;space=0;lis=[]
        for _ in line:
            #print(_,end='')
            if flag==0 and _=='<':
                flag=1
            elif flag==1 and _=='>':
                if slash==1:
                    slash=0
                    if head!='br ':
                        #print(lis[-1],head)
                        if lis.pop()!=head:
                            TF=1;break
                    head=''
                else:
                    lis.append(head)
                    head=''
                    space=0
                flag=0
            
            if flag==1 and _!='<':
                if _=='/' and head!='a':
                    slash=1
                elif _==' ' and head=='a':
                    space=1
                elif space==0:
                    head+=_
        #print()
    except:TF=1
    #print(line,TF,lis)
    print(['','il'][TF or len(lis)>0]+'legal')
    line=input()
