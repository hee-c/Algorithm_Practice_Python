import sys
n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
x = [[0]*(n+1) for _ in range(n+1)]
result = []

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    x[a][b], x[b][a] = 1, 1

def dfs(d):
    result.append(d)
    for i in range(1, n+1):
        if i not in result and x[d][i] == 1:
            dfs(i)

    return len(result) - 1

print(dfs(1))