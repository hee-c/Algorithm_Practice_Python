def dfs0(v, x, y):
    if x <= -1 or x >= len(v) or y <= -1 or y >= len(v[0]):
        return False
    if v[x][y] == 0:
        v[x][y] = 3
        dfs0(v, x-1, y)
        dfs0(v, x, y-1)
        dfs0(v, x+1, y)
        dfs0(v, x, y+1)
        return True
    return False

def dfs1(v, x, y):
    if x <= -1 or x >= len(v) or y <= -1 or y >= len(v[0]):
        return False
    if v[x][y] == 1:
        v[x][y] = 3
        dfs1(v, x-1, y)
        dfs1(v, x, y-1)
        dfs1(v, x+1, y)
        dfs1(v, x, y+1)
        return True
    return False

def dfs2(v, x, y):
    if x <= -1 or x >= len(v) or y <= -1 or y >= len(v[0]):
        return False
    if v[x][y] == 2:
        v[x][y] = 3
        dfs2(v, x-1, y)
        dfs2(v, x, y-1)
        dfs2(v, x+1, y)
        dfs2(v, x, y+1)
        return True
    return False

def solution(v):
    result = [0, 0, 0]

    if len(v) == 1:
        if v[0] == [0]:
            result[0] += 1
        elif v[0] == [1]:
            result[1] += 1
        elif v[0] == [2]:
            result[2] += 1
        return result

    for i in range(len(v)):
        for j in range(len(v[0])):
            if dfs0(v, i, j) == True:
                result[0] += 1
            elif dfs1(v, i, j) == True:
                result[1] += 1
            elif dfs2(v, i, j) == True:
                result[2] += 1

    answer = result
    return answer

print(solution([[0]]))
