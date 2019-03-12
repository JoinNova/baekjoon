#boj2908 Will It Stop?
n=int(input())
while 1:
    if n//2==n/2:n//=2
    else:break
print(['TAK','NIE'][n>1])

#02
n=int(input())
while 2<n:n/=2
print('TNAIKE'[2>n::2])

#by jh05013
print("TAK" if bin(int(input())).count('1') == 1 else "NIE")

#by jh05013 modified by Nova
print("NTIAEK"[2>bin(int(input())).count('1')::2])
