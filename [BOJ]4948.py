import sys

def prime_list(n):
    if n == 1:
        return 1

    sieve = [True] * (n * 2)

    m = int((n*2) ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i * 2, n*2, i):
                sieve[j] = False

    return len([i for i in range(n+1, n*2) if sieve[i] == True])

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    print(prime_list(n))

# def prime_number(n):
#     total = 0

#     for i in range(n+1, (2 * n) + 1):
#         if i % 2 == 0:
#             continue
#         isPrime = True
#         for j in range(2, i // 2):
#             if i % j == 0:
#                 isPrime = False
#                 break
#         if isPrime:
#             total += 1

#     return total

# def is_prime_number(n):
#     if n % 2 == 0:
#         return False
#     for i in range(3, n, 2):
#         if n % i == 0:
#             return False
#     return True

# def eratos(n):
#     codomain = list(range(3, n+1, 2))
#     prime = [2]

#     while True:
#         p = codomain.pop(0)
#         prime.append(p)
#         m = int(n ** 0.5)
#         for i in range(2, m+1):
#             if i >= len(codomain):
#                 break
#             if codomain[i] % p == 0:
#                 del codomain[i]

#         if len(codomain) == 0:
#             break

#     return len(prime)
