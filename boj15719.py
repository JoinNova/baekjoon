#by jh05013 Python3
from sys import stdin
def read():
    while 1:
        s = stdin.read(100000)
        if not s: return
        while s[-1] != ' ':
            extra = stdin.read(1)
            if not extra: break
            s+= extra
        yield from map(int, s.split())

n = int(input())
s = n*(n-1)//2
for x in read(): s-= x
print(-s)
