#boj1697 숨바꼭질
from collections import deque
def bfs(n,k):
    limit=100000
    visit=[-1]*100001
    visit[n]=False
    q=deque()
    q.append(n)
    while q:
        cur=q.popleft()
        for _ in [cur-1,cur+1,cur*2]:
            if 0<=_<=limit and visit[_]==-1:
                q.append(_)
                visit[_]=visit[cur]+True
    return visit[k]
    
n,k=map(int,input().split())
print(bfs(n,k))
