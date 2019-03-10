#boj15873_공백 없는 A+B
t=input();i=int;r=20
if len(t)<3:
    r=i(t[0])+i(t[1])
elif len(t)<4:
    r=10+[i(t[-1]),i(t[0])][t[-1]=='0']
print(r)

#by shiftpsh
print(sum(ord(c)-39for c in input())-18)

#by joonas
s=input();print(sum(list(map(int,(s[0], s[1:]) if s[1]!='0' else (s[:2], s[2:])))))
