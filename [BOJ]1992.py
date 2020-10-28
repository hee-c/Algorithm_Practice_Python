import sys
n = int(input())
video = []
for i in range(n):
    video.append(list(input()))
output=''

def comp(x,y,z):
    global output
    check = video[x][y]

    for i in range(x, x+z):
        for j in range(y, y+z):
            if check != video[i][j]:
                output += '('
                comp(x, y, z//2)
                comp(x, y+z//2, z//2)
                comp(x+z//2, y, z//2)
                comp(x+z//2, y+z//2, z//2)
                output += ')'
                return

    if check == '1':
        output += '1'
        return
    else:
        output += '0'
        return

comp(0,0,n)
print(output)