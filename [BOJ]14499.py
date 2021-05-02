n, m, y, x, k = map(int, input().split())
field = []

for _ in range(n):
  temp = list(map(int, input().split()))
  field.append(temp)

order_queue = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]

while order_queue:
  order = order_queue.pop(0)

  if order == 1:
    if x+1 >= 0 and x+1 < m and y >= 0 and y < n:
      x += 1
      dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
      print(dice[1])
      if field[y][x] == 0:
        field[y][x] = dice[6]
      else:
        dice[6] = field[y][x]
        field[y][x] = 0
    else:
      continue
  elif order == 2:
    if x-1 >= 0 and x-1 < m and y >= 0 and y < n:
      x -= 1
      dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
      print(dice[1])
      if field[y][x] == 0:
        field[y][x] = dice[6]
      else:
        dice[6] = field[y][x]
        field[y][x] = 0
    else:
      continue
  elif order == 3:
    if x >= 0 and x < m and y-1 >= 0 and y-1 < n:
      y -= 1
      dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
      print(dice[1])
      if field[y][x] == 0:
        field[y][x] = dice[6]
      else:
        dice[6] = field[y][x]
        field[y][x] = 0
    else:
      continue
  elif order == 4:
    if x >= 0 and x < m and y+1 >= 0 and y+1 < n:
      y += 1
      dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
      print(dice[1])
      if field[y][x] == 0:
        field[y][x] = dice[6]
      else:
        dice[6] = field[y][x]
        field[y][x] = 0
    else:
      continue
