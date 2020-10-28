import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if field[x][y] == 1:
        field[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x-1, y-1)
        dfs(x+1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y+1)
        return True
    return False


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    field = list()
    for i in range(h):
        field.append(list(map(int, sys.stdin.readline().split())))

    result = 0

    for j in range(h):
        for l in range(w):
            if dfs(j, l) == True:
                result += 1

    print(result)