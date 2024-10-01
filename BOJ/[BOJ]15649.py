import sys
n, m = map(int, sys.stdin.readline().split())
check = [False]*(n+1)
result = [0] * m

def func(index, n, m):
    if index == m:
        for i in range(m):
            print(result[i], end=' ')
        print()
        return

    for i in range(1, n+1):
        if check[i]:
            continue
        check[i] = True
        result[index] = i
        func(index+1, n, m)
        check[i] = False

func(0, n, m)