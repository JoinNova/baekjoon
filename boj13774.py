#boj13774 Palindromes
txt=input()
while txt!='#':
    chk=0
    for i in range(len(txt)):
        case=txt[:i]+txt[i+1:]
        #print(case[:len(case)//2],case[len(case)//2:])
        if len(case)%2==0:
            if case[:len(case)//2]==case[len(case)//2:][::-1]:
                chk=1
                break
        else:
            if case[:len(case)//2]==case[len(case)//2+1:][::-1]:
                chk=1
                break
    print(['not possible',case][chk])
    txt=input()
