import sys
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    arrayN = set(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    arrayM = list(map(int,sys.stdin.readline().split()))

    for i in arrayM:
        if i in arrayN:
            print(1)
        else:
            print(0)