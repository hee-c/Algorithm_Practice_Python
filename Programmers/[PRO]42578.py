from itertools import combinations
from functools import reduce
import math

def multiply(arr):
  result = 1
  for x in arr:
        result = result * x
  return result
  # return reduce(lambda x, y: x * y, arr)

def solution(clothes):
  closet = {}
  items = []
  answer = 0

  for item in clothes:
    temp = closet.keys()
    if (item[1] not in temp):
      closet[item[1]] = 1
    else:
      closet[item[1]] += 1


  for genre in closet.keys():
    items.append(closet[genre])


  for i in range(1, len(items) + 1):
    temp = list(combinations(items, i))
    for j in temp:
      answer += multiply(j)

  return(answer)

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
