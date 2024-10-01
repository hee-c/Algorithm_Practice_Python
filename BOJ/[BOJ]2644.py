from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())
m = int(input())

relation = [[] for _ in range(n+1)]
dist = [0] * (n+1)

for i in range(m):
    parent, child = map(int, input().split())
    relation[parent].append(child)
    relation[child].append(parent)

def bfs():
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for i in relation[now]:
            if dist[i] == 0:
                q.append(i)
                dist[i] = dist[now] + 1
            if i == end:
                return dist[i]
    return -1

print(bfs())
