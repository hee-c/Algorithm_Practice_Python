def solution(prices):
  hold = [{'condition': True, 'days': 1} for i in range(len(prices) - 1)]
  hold.append({'condition': True, 'days': 0})

  for i in range(1, len(prices) - 1):
    for j in range(i):
      if (prices[j] <= prices[i] and hold[j]['condition']):
        hold[j]['days'] += 1
      else:
        hold[j]['condition'] = False

  answer = []
  for i in range(len(prices)):
    answer.append(hold[i]['days'])

  return answer



print(solution([1, 2, 3, 2, 3]))
print(solution([2, 3, 1, 4, 5]))
