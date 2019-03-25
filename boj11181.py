#boj11181 Base-2 Palindromes
n=int(input())-1;i=1
while(1):
    firstbit=1<<(i-1)//2
    if n>=firstbit:
        n-=firstbit
    else:
        Palindrome=n+(1<<((i-1)//2))
        n//=1+(i%2)
        for j in range(i%2,(i-1)//2):
            Palindrome=Palindrome*2+n%2
            n//=2
        Palindrome=[Palindrome,Palindrome*2+1][i>1]          
        print(Palindrome)
        break
    i+=1
