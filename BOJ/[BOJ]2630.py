import sys
n=int(sys.stdin.readline())
color_paper=[]
white=0
blue=0

for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    color_paper.append(a)

def cut(x,y,n):
    global blue,white
    check=color_paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=color_paper[i][j]:
                cut(x,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y,n//2)
                cut(x+n//2,y+n//2,n//2)
                return


    if check==0:
        white+=1
        return
    else:
        blue+=1
        return

cut(0,0,n)
print(white)
print(blue)