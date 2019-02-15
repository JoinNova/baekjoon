#boj3055 탈출
#by chemistrae03
from copy import deepcopy
r,c=map(int,input().split())
b=[]
v=[[False for _ in range(c)] for _ in range(r)]
p,z=0,0
for i in range(r):
 a=list(input());b.append(a)
 if "S" in a:p=(a.index("S"),i)
q=[(p,b,0)]
dx=(-1,1,0,0);dy=(0,0,-1,1)
while q:
 x=q[0][0][0];y=q[0][0][1];cb=q[0][1];m=q[0][2];q.pop(0)
 if b[y][x]=="D":z=m;break
 nb=deepcopy(cb)
 for i in range(r):
  for j in range(c):
   if cb[i][j]=="*":
    for k in range(4):
     nwx=j+dx[k]; nwy=i+dy[k]
     if not (0<=nwx<c and 0<=nwy<r) or (cb[nwy][nwx]=="X" or cb[nwy][nwx]=="D"):continue
     nb[nwy][nwx]="*"
 for i in range(4):
  nx= x + dx[i]; ny= y + dy[i]
  if not (0<=nx<c and 0<=ny<r) or (v[ny][nx] or nb[ny][nx]=="X" or nb[ny][nx]=="*"):continue
  v[ny][nx]=True;q.append(((nx,ny),nb,m+1))
if z!=0:print(m)
else:print("KAKTUS")


#by kitae135
import sys
from collections import deque

r, c = map(int, sys.stdin.readline().strip().split())

water = [[0 for __ in range(c)] for _ in range(r)]
queue = deque()
alive = deque()

for i in range(r):
    row = list(sys.stdin.readline().strip())
    for j in range(c):
        if row[j] == '.':
            pass # 물이 없는 곳은 0 그대로

        elif row[j] == '*':
            water[i][j] = 1 # 물이 들어 찬 곳
            queue.append((i, j)) # 물은 범람시켜야 하므로 큐에 저장

        elif row[j] == 'X':
            water[i][j] = -1 # 막힌 곳(돌)은 -1

        elif row[j] == 'D':
            water[i][j] = -1 # 목적지도 물 입장에선 막힌 곳
            goal = (i, j) # 목적지

        elif row[j] == 'S':
            alive.append((i, j)) # 살아남아있는 고슴도치들의 위치

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
moved = 0

# 큐들에 원소가 한개라도 있으면 진행
while len(queue) + len(alive) > 0:

    # 물 범람 1회 진행
    nextQueue = deque()
    while len(queue) != 0:
        tu = queue.popleft()
        for i in range(4):
            x = tu[0] + dx[i]
            y = tu[1] + dy[i]

            # 맵 안이고, 물이 범람할 수 있는 곳이면, 물이 들어참
            if 0 <= x < r and 0 <= y < c and (water[x][y] == 0 or water[x][y] == 2):
                water[x][y] = 1
                nextQueue.append((x, y))
    queue = nextQueue

    # 고슴도치 1보 전진
    if len(alive) == 0:
        print("KAKTUS")
        exit(0)

    moved += 1
    nextAlive = deque()
    while len(alive) != 0:
        tu = alive.popleft()
        #water[tu[0]][tu[1]] = 2 # 이미 지나온곳은 다시 갈필요 없으므로

        for i in range(4):
            x = tu[0] + dx[i]
            y = tu[1] + dy[i]

            # 목적지 도착 여부 검사
            if (x, y) == goal:
                print(moved)
                exit(0)

            # 맵 안이고 물이 없으면 전진
            if 0 <= x < r and 0 <= y < c and water[x][y] == 0:
                water[x][y] = 2
                nextAlive.append((x, y))

    alive = nextAlive

print("KAKTUS")

#by jh05013
from collections import deque

def get(L, i, j):
    if 0<=i<len(L) and 0<=j<len(L[0]): return L[i][j]
    return "X"

def bfs():
    for TIME in range(len(Q)):
        i, j, c = Q.popleft()
        if grid[i][j] != c: continue
        for ni, nj in (i-1,j), (i+1,j), (i,j-1), (i,j+1):
            a, b = grid[i][j], get(grid, ni, nj)
            if a+b in ("S.", "*.", "*S"):
                grid[ni][nj] = a
                Q.append((ni,nj,a))
            elif a+b == "SD":
                return True
    return False

r, c = map(int,input().split())
Q = deque()
grid = []
water = []
for i in range(r):
    row = input()
    for j in range(c):
        if row[j] == "*": water.append((i,j))
        elif row[j] == "S": Q.append((i,j,"S"))
    grid.append(list(row))
for i, j in water: Q.append((i,j,"*"))

for i in range(r*c):
    if bfs():
        print(i+1)
        break
else: print("KAKTUS")

#by hello70825
from collections import deque
r,c=map(int,input().split())
S=[input() for _ in range(r)]
dx,dy=[0,0,1,-1],[1,-1,0,0]
water_D=[[-1]*c for _ in range(r)]
D=[[-1]*c for _ in range(r)]
q=deque()
for i in range(r):
    for j in range(c):
        if S[i][j]=='*':q.append((i,j));water_D[i][j]=0
        elif S[i][j]=='S':sx,sy=i,j
        elif S[i][j]=='D':ex,ey=i,j
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and S[nx][ny] not in 'DX' and water_D[nx][ny]==-1:
            water_D[nx][ny]=water_D[x][y]+1;q.append((nx,ny))
q.append((sx,sy));D[sx][sy]=0
while q:
    x,y=q.popleft()
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx<r and 0<=ny<c and D[nx][ny]==-1 and S[nx][ny] not in '*X':
            if water_D[nx][ny]==-1 or D[x][y]+1<water_D[nx][ny]:
                D[nx][ny]=D[x][y]+1;q.append((nx,ny))
print([D[ex][ey],'KAKTUS'][D[ex][ey]==-1])
