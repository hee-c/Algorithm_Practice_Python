import sys

n = int(sys.stdin.readline())
arrayN = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arrayM = list(map(int, sys.stdin.readline().split()))

def binart_sreach(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

result = [0] * 20000004

test = sorted(arrayM)

for i in range(n):
    temp_answer = binart_sreach(test, arrayN[i], 0, m-1)
    if temp_answer != None:
        result[arrayN[i]+10000001] += 1

for i in arrayM:
    print(result[i+10000001], end=" ")
