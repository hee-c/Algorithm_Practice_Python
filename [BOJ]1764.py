import sys

n, m = map(int, sys.stdin.readline().split())
arrayN = [0 for _ in range(n)]
arrayM = [0 for _ in range(m)]

for i in range(n):
    arrayN[i] = sys.stdin.readline().rstrip()

for i in range(m):
    arrayM[i] = sys.stdin.readline().rstrip()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return target
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

dbj = []

if n >= m:
    arrayN.sort()
    for i in arrayM:
        result = binary_search(arrayN, i, 0, n-1)
        if result != None:
            dbj.append(result)
else:
    arrayM.sort()
    for i in arrayN:
        result = binary_search(arrayM, i, 0, m-1)
        if result != None:
            dbj.append(result)


dbj.sort()
print(len(dbj))
for i in dbj:
    print(i)
