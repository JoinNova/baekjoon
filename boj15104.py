#boj15104 Odd Palindrome
t=input();print(['Or not.','Odd.'][all([_!=_[::-1]for _ in[t[i:j]for i in range(len(s))for j in range(i+2,len(t)+1,2)]])])
