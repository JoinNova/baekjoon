#boj1467 수지우기
from collections import*

default=input()
printdigit = Counter(default)-Counter(input())
ordnum=0

while printdigit:
    digit = chr(57-ordnum)
    idx = default.find(digit)
    
    if -1 < idx:
        if idx != Counter(digit)-printdigit:
            if Counter(digit)-printdigit == printdigit-Counter(default[idx:]):
                print(digit,end='')
                default = default[idx+1:]
                ordnum=-1
                printdigit -= Counter ( digit )

    ordnum+=1



##############
from collections import*

default=input()
printdigit = Counter(default)-Counter(input())
ordnum=0

while printdigit:
    TrueFalse = False
    digit = chr(57-ordnum)
    idx = default.find(digit)
    
    if -1 < idx:
        if idx != Counter(digit)-printdigit:
            if Counter(digit)-printdigit == printdigit-Counter(default[idx:]):
                TrueFalse = True
                print(TrueFalse*digit,end='')
                default = default[idx+1:]
                ordnum=0
            
    printdigit -= Counter ( TrueFalse*digit )

    #default = default[-~idx*TrueFalse:]
    #[-~2:] 앞쪽부터 슬라이싱
    if TrueFalse:
        continue
    else:
        ordnum+=1
    #ordnum = ~ordnum*~-TrueFalse
