#boj6588 골드바흐의추정
#t=440ms
import sys;input=sys.stdin.readline

def sear(t,l,sieve):
    for _ in l:
        q=t-_
        if sieve[q]:
            print(str(t)+' = '+str(_)+' + '+str(q))
            return
        
sieve = list(range(1000000))
sieve[1] = 0
for p in range(2, int(1000000**0.5)+1):
    if sieve[p] != 0:
        for q in range(2*p, 1000000, p):
            sieve[q] = 0
l=[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599]
lis=[]
while 1:
    t=int(input())
    if t==0:break
    lis.append(t)
for _ in lis:
    sear(_,l,sieve)
    

#by milkclouds
# t=372ms
import sys
input=sys.stdin.readline

p=[0,0,1,1]+[1]*(1000000-3)

p[4::2]=[0]*(10**6//2-1)
p[6::3]=[0]*(10**6//3-1)
for i in range(5,1000000):
	if p[i]==1:
		if i%6 not in (1,5):
			p[i]=0
		else:
			p[i+i::i]=[0]*(10**6//i-1)
#			for a in range(2,i**0.5+1):
#				if i%a==0: 


while 1:
	i=int(input())
	if i==0: break
	for a in range(i,i//2-1,-1):
		if p[a]:
			b=(i-a)
			if p[b]:
				print('%d = %d + %d'%(i,b,a))
				break
