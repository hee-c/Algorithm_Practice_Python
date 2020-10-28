import sys

n = int(sys.stdin.readline())
stair = [0] * 301
cnt = 0
score = 0
idx = 0

for i in range(1, n+1):
    stair[i] = int(sys.stdin.readline())

while (idx <= n):
    if idx == n-2 and cnt == 1:
        score += stair[idx+2]
        idx += 2
    else:
        if cnt == 0:
            if stair[idx+1] + stair[idx+2] > stair[idx+3]:
                score += (stair[idx+1] + stair[idx+2])
                idx += 2
                cnt += 2
            else:
                if stair[idx+1] > stair[idx+2]:
                    score += stair[idx+1]
                    idx += 1
                    cnt += 1
                else:
                    score += stair[idx+2]
                    idx += 2
                    cnt = 0
        elif cnt == 1:
            if stair[idx+1] > stair[idx+2]:
                score += stair[idx+1]
                idx += 1
                cnt += 1
            else:
                score += stair[idx+2]
                idx += 2
                cnt = 0
        else:
            score += stair[idx+2]
            idx += 2
            cnt = 0
print(score)