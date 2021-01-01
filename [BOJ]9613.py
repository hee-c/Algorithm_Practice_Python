from itertools import combinations

t = int(input())

for i in range(t):
    num = list(map(int, input().split()))
    total = []

    for a, b in list(combinations(num[1:], 2)):
        maximum = 1
        if a == b:
            total.append(a)
            continue
        elif a > b:
            for j in range(2, b+1):
                if a % j == 0 and b % j == 0:
                    maximum = j
        else:
            for j in range(2, a+1):
                if b % j == 0 and a % j == 0:
                    maximum = j
        total.append(maximum)
    print(sum(total))
