import sys
n = int(sys.stdin.readline())
x = []

for i in range(n):
    x.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
    for j in range(len(x[i])):
        if j == 0:
            x[i][j] += x[i-1][0]
        elif j == len(x[i])-1:
            x[i][j] += x[i-1][len(x[i-1])-1]
        else:
            if x[i-1][j-1] == x[i-1][j]:
                x[i][j] += x[i-1][j-1]
            elif x[i-1][j-1] > x[i-1][j]:
                x[i][j] += x[i-1][j-1]
            else:
                x[i][j] += x[i-1][j]


print(max(x[n-1]))