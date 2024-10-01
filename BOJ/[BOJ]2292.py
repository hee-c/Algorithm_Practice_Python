n = int(input())

def solution(n):
  if (n == 1):
    return 1
  
  times = 1
  limit = 1

  while True:
    limit = limit + (times * 6)

    if (n <= limit):
      return times +1

    times += 1

print(solution(n))
