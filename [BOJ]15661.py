from itertools import combinations

n = int(input())
abil = []
x = list(range(n))

for i in range(n):
  temp = list(map(int, input().split()))
  abil.append(temp)

minimum = 99999

def solution():
  global n, abil, x, minimum

  for i in range(1, (n//2)+1):
    for j in combinations(x, i):
      temp = x[:]
      for k in j:
        temp.remove(k)

      # j가 스타트 팀
      # temp가 링크 팀

      start = 0
      link = 0

      if len(j) != 1:
        start_list = combinations(j, 2)
        start_temp = 0
        for a, b in start_list:
          start_temp += (abil[a][b] + abil[b][a])
        start = start_temp

      if len(temp) != 1:
        link_list = combinations(temp, 2)
        link_temp = 0
        for a, b in link_list:
          link_temp += (abil[a][b] + abil[b][a])
        link = link_temp

      candidate = abs(start - link)

      if candidate < minimum:
        minimum = candidate
      if candidate == 0:
        return 0

  return minimum

print(solution())
