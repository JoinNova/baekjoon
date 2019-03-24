#boj11286 절대값힙
import heapq
import sys;s=sys.stdin.readline
lis=[]
for i in range(int(s())):
    element=int(s())
    if element==0:
        print(heapq.heappop(lis)[1]if lis else 0)
    else:
        heapq.heappush(lis,(abs(element),element))
