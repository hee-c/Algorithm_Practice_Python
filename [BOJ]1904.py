import sys

a = [0]*1000001
a[0]=1
a[1]=2
n = int(sys.stdin.readline())
for i in range(2,n):
    a[i] = (a[i-1]+a[i-2])%15746

print(a[n-1])