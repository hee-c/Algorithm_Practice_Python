import sys
n = int(sys.stdin.readline())
x = [0, 1]

for _ in range(n-1):
    x.append(x[len(x)-1]+x[len(x)-2])

print(x[len(x)-1])