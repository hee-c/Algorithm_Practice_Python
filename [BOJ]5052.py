import sys
t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())
    idx = [0 for _ in range(n+1)]
    idx[0] = -2
    array = [0 for _ in range(n)]
    totalString = ''

    for j in range(n):
        array[j] = sys.stdin.readline().rstrip()
        idx[j+1] = len(array[j])
        totalString += array[j]

    status = 0

    for k in array:
        idx2 = totalString.find(k)
        if idx2 in idx and k == totalString[idx2-1:idx2+len(k)]:
            pass
        else:
            print('NO')
            status=1
            break
    if status == 0:
        print('YES')