#boj6474 Palindromes
mir='AEHIJLMOSTUVWXYZ12358BCDFGKNPQR4679';rev='A3HILJMO2TUVWXY51SEZ8BCDFGKNPQR4679'

try:
    while 1:
        chk1=0;chk2=0
        txt=input()
        long=len(txt)
        for i in range(long//2):
            if txt[i]==txt[long-i-1]:
                chk1+=1
            if mir.index(txt[i])==rev.index(txt[long-i-1]) or rev.index(txt[i])==mir.index(txt[long-i-1]):
                if mir.index(txt[i])<21:
                    if rev.index(txt[long-i-1])<21:
                        chk2+=1
                elif rev.index(txt[i])<21:
                    if mir.index(txt[long-i-1])<21:
                        chk2+=1
        if long!=1:
            if chk1==long//2:
                if chk2==long//2:
                    print(txt,'-- is','a mirrored palindrome.\n')
                else:
                    print(txt,'-- is','a palindrome.\n')
            else:
                if chk2==long//2 and long%2!=0:
                    print(txt,'-- is','a mirrored string.\n')
                else:
                    print(txt,'-- is','not a palindrome.\n')
        else:
            if mir.index(txt)<21:
                print(txt,'-- is','a mirrored palindrome.\n')
            else:
                print(txt,'-- is','a palindrome.\n')
                
  
except:exit()
