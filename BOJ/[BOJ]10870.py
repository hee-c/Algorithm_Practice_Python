def fibo(n):
    if n >= 2:
        return fibo(n-1) + fibo(n-2)
    elif n == 1:
        return 1
    else:
        return 0

num=int(input())
print(fibo(num))