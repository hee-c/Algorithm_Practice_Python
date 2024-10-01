import sys
n = int(sys.stdin.readline())
array = [0 for _ in range(10001)]

for _ in range(n):
    temp = int(sys.stdin.readline())
    array[temp] += 1

for i in range(10001):
    if array[i] == 0:
        pass
    else:
        for j in range(array[i]):
            print(i)