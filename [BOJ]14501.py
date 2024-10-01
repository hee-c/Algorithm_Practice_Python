n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)

for i in range(1, n+1):
  t[i], p[i] = map(int, input().split())

cnt = 1
money = 0

while True:
  if cnt > n:
    break

  if t[cnt] == 1:
    money += p[cnt]
    cnt += 1
    continue

  if cnt == n:
    break

  temp1 = 0
  temp2 = 0

  if cnt + t[cnt] - 1 <= n:
    temp1 += p[cnt]
  if cnt + t[cnt] <= n:
    if cnt + t[cnt] + t[cnt + t[cnt]] - 1 <= n:
      temp1 += p[cnt + t[cnt]]

  if cnt + 1 + t[cnt+1] - 1 <= n:
    temp2 += p[cnt+1]
  if cnt + 1 + t[cnt+1] <= n:
    if cnt + 1 + t[cnt+1] + t[cnt + 1 + t[cnt+1]] - 1 <= n:
      temp2 += p[cnt + 1 + t[cnt+1]]

  if temp1 == 0 and temp2 == 0:
    break

  if temp1 >= temp2:
    money += p[cnt]
    cnt += t[cnt]
  else:
    money += p[cnt+1]
    cnt += t[cnt+1] + 1

print(money)
