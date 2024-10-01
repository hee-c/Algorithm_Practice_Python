

def solution (a, b, v):
  left_height = v - a
  climb = a - b
  day = 1

  if (left_height) <= 0:
    return day

  if (left_height % climb == 0):
    return day + (left_height // climb)
  else:
    return day + (left_height // climb) + 1

a, b, v = map(int, input().split())
print(solution(a, b, v))
