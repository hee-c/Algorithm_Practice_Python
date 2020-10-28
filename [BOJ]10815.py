import sys

n = int(sys.stdin.readline())
arrayN = list(map(int, sys.stdin.readline().split()))
arrayN.sort()

m = int(sys.stdin.readline())
arrayM = list(map(int, sys.stdin.readline().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in arrayM:
    if binary_search(arrayN, i, 0, n-1) == None:
        print(0, end=" ")
    else:
        print(1, end=" ")
