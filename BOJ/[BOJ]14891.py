wheels = [[]]

for i in range(4):
  temp = list(input())
  wheels.append(temp)

k = int(input())

def rotate(num, direction):
  global wheels
  if direction == 1:
    wheels[num].insert(0, wheels[num][7])
    wheels[num].pop()
  if direction == -1:
    wheels[num].append(wheels[num].pop(0))


for i in range(k):
  num, direction = map(int, input().split())

  condition_1 = wheels[1][2] != wheels[2][6]
  condition_2 = wheels[2][2] != wheels[3][6]
  condition_3 = wheels[3][2] != wheels[4][6]

  if num == 1:
    rotate(1, direction)
    if condition_1:
      rotate(2, -direction)
      if condition_2:
        rotate(3, direction)
        if condition_3:
          rotate(4, -direction)

  elif num == 2:
    rotate(2, direction)
    if condition_1:
      rotate(1, -direction)
    if condition_2:
      rotate(3, -direction)
      if condition_3:
        rotate(4, direction)

  elif num == 3:
    rotate(3, direction)
    if condition_3:
      rotate(4, -direction)
    if condition_2:
      rotate(2, -direction)
      if condition_1:
        rotate(1, direction)

  elif num == 4:
    rotate(4, direction)
    if condition_3:
      rotate(3, -direction)
      if condition_2:
        rotate(2, direction)
        if condition_1:
          rotate(1, -direction)

total = 0
for i in range(1, 5):
  if wheels[i][0] == '1':
    total += 2**(i-1)

print(total)

# 12시 = 0번
# 3시 = 2번
# 9시 = 6번
