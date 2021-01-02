n, k = map(int, input().split())
x = list(range(1,n+1))
y = []
target = -1
while len(x) != 0:
    target += k-1
    if target > len(x)-1:
        while target > len(x)-1:
            target -= len(x)
    y.append(x[target])
    del x[target]

print('<'+','.join(map(str, y))+'>')