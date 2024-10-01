import sys

n, k = map(int, sys.stdin.readline().split())
codomain = list(range(2, n+1))
deleted = []

while True:
    p = codomain.pop(0)
    deleted.append(p)

    for i in range(len(codomain)):
        if i >= len(codomain):
            break
        if codomain[i] % p == 0:
            deleted.append(codomain.pop(i))

    if len(codomain) == 0:
        break

print(deleted[k-1])
