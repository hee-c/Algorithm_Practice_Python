import sys
n, m = map(int, sys.stdin.readline().split())
check = [False] * n
result = []

def func(depth, idx, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(idx, n):
        if not check[i]:
            check[i] = True
            result.append(i+1)
            func(depth+1, i+1, n, m)
            check[i] = False
            result.pop()
func(0, 0, n, m)