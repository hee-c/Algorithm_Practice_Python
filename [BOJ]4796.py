cnt = 1

while True:
  l, p, v = map(int, input().split())
  vacation = 0

  if l == 0 and p == 0 and v == 0:
    break

  vacation += (v // p) * l

  if v % p != 0:
    vacation += min(v % p, l)

  print(f'Case {cnt}: {vacation}')

  cnt += 1
