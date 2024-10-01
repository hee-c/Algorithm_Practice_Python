import sys
n = int(sys.stdin.readline())
dots = [0] * n

for i in range(n):
    dots[i] = list(map(int, sys.stdin.readline().split()))

dots.sort()

searched = [0]
last = 0
total = 0

for i in range(n):
    if i == 0:
        searched.append(dots[i][0])
        last = dots[i][1]
        continue

    if dots[i][0] != searched[-1]:
        if dots[i][0] > last:
            total += last - searched[-1]
            searched.append(dots[i][0])
            last = dots[i][1]
        else:
            total += (last - dots[i][0]) - searched[-1] + 1
            searched.append(dots[i][0])
            last = dots[i][1]
    else:
        last = dots[i][1]

    if i == n - 1:
                total += last - searched[-1]

print(total)
