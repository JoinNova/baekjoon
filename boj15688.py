#boj15688 수정렬하기 
#import time
#import sys;s=sys.stdin.readline
#start=time.time()
#print ('\n'.join(map(str,l)))
#print(*l,sep='\n')
#print(time.time()-start)

import sys;s=sys.stdin.readline
l=[int(s())for _ in '_'*int(s())];l.sort()
print ('\n'.join(map(str,l)))


import sys;s=sys.stdin.readline
print ('\n'.join(map(str,sorted(int(s())for _ in '_'*int(s())))))

#by milkclouds
import sys;import time;start=time.time();l=[5,5,4,3,2,1]
print('\n'.join(map(str,sorted(map(int,l[1:])))))
print(time.time()-start)
