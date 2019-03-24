#boj11270 최대 힙
import heapq
import sys;s=sys.stdin.readline
lis=[]
for _ in'_'*int(s()):
    element=int(s())
    if element==0:
        print(heapq.heappop(lis)[1]if lis else 0)
    else:
        heapq.heappush(lis,(-element,element))
        
        
