#12833 XORXORXOR
a,b,c=map(int,input().split());exec('a=a^b'*(c%2));print(a)

#02
a,b,c=map(int,input().split());print([a,a^b][c%2])
