import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if field[x][y] == 1:
        field[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

t = int(sys.stdin.readline())
ans = list()

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        tempX, tempY = map(int, sys.stdin.readline().split())
        field[tempY][tempX] = 1

    result = 0

    for j in range(n):
        for l in range(m):
            if dfs(j, l) == True:
                result += 1

    ans.append(result)

for kk in ans:
    print(kk)