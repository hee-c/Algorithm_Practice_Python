x = int(input())

def solution(x):
  answer = 0
  index = 1

  while True:
    answer += index

    if (answer >= x):
      if (index % 2 == 0):
        return f'{index - (answer - x)}/{1 + (answer - x)}'
      else:
        return f'{1 + (answer - x)}/{index - (answer - x)}'

    index += 1

print(solution(x))
