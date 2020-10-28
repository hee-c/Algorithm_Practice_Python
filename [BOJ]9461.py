import sys

t = int(sys.stdin.readline())
x = [0] * 101
x[1] = 1
x[2] = 1
x[3] = 1
x[4] = 2
x[5] = 2

for i in range(t):
    n = int(sys.stdin.readline())
    if x[n] != 0:
        print(x[n])
    else:
        for j in range(6,n+1):
            x[j] = x[j-1] + x[j-5]
        print(x[n])