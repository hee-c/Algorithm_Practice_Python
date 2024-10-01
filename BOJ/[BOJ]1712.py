import sys
a, b, c = map(int, sys.stdin.readline().split())

if b < c:
    sales = a // (c - b)
    while (a + (b * sales)) >= (c * sales):
        sales += 1
    print(sales)
else:
    print(-1)



a, b, c = map(int, sys.stdin.readline().split())
if (c-b) != 0:
    sales = a // (c - b)
    while (a + (b * sales)) >= (c * sales):
        sales += 1

if (a + (b * sales)) >= (c * sales):
    print(-1)
else:
    print(sales)
