import sys, bisect

n = int(sys.stdin.readline())
arrayA = [0 for _ in range(n)]
arrayB = [0 for _ in range(n)]
arrayC = [0 for _ in range(n)]
arrayD = [0 for _ in range(n)]

for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    arrayA[i] = temp[0]
    arrayB[i] = temp[1]
    arrayC[i] = temp[2]
    arrayD[i] = temp[3]

arrayA.sort()
arrayB.sort()
arrayC.sort()
arrayD.sort()

total = 0
result = 0
x = 268435456

for i in arrayA:
    for j in arrayB:
        if i+j >= 0:
            for k in arrayC[:bisect.bisect_left(arrayC, x-(i+j))]:
                for l in arrayD[bisect.bisect_left(arrayD, -(i+j+k)):]:
                    if i+j+k+l == 0:
                        result += 1
                    else:
                        break
        else:
            for k in arrayC[bisect.bisect_left(arrayC, x-(i+j)):]:
                for l in arrayD[bisect.bisect_left(arrayD, -(i+j+k)):]:
                    if i+j+k+l == 0:
                        result += 1
                    else:
                        break

print(result)