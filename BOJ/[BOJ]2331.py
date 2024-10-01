import sys
a, p = map(int,sys.stdin.readline().split())
x = [a,]

while True:
    temp = 0
    for i in str(x[len(x)-1]):
        temp += int(i)**p
    if temp not in x:
        x.append(temp)
    else:
        break

print(x.index(temp))