import sys
n, l, r = int(sys.stdin.readline().split())
field = [0] * n

for i in range(n):
    field[i] = list(map(int, sys.stdin.readline().split()))
