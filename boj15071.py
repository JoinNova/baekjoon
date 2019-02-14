#boj1571 The Key to Cryptography
import sys;s=sys.stdin.readline

def conv(te,ke):
    if ord(te)-ord(ke)<0:
        return chr(ord(te)-ord(ke)+91)
    return chr(ord(te)-ord(ke)+65)

ciphertext=s().strip()
key=s().strip()
for _ in ciphertext:
    print(conv(_,key[0]),end='')
    key=key[1:]+conv(_,key[0])
    
#02
def v(t,k):
 if ord(t)-ord(k)<0:return chr(ord(t)-ord(k)+91)
 return chr(ord(t)-ord(k)+65)
c=input();k=input()
for _ in c:print(v(_,k[0]),end='');k=k[1:]+v(_,k[0])
