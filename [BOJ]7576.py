import sys, copy
from collections import deque

m, n = map(int, sys.stdin.readline().split())
box = [0 for _ in range(n)]
data = list()

for i in range(n):
    box[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(m):
        if box[i][j] == 1:
            data.append((0,i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque(data)

while q:
    time, x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = 1
                q.append((time+1, nx, ny))

status = 0

for i in box:
    if 0 in i:
        status = 1

if status == 1:
    print(-1)
else:
    print(time)