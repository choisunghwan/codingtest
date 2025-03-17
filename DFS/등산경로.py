import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y):
    global cnt
    if x==ex and y==ey:
        cnt+=1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0<=xx<n and 0<=yy<n and check[xx][yy]==0 and board[x][y] < board[xx][yy]:
                check[xx][yy]=1
                DFS(xx,yy)
                check[xx][yy]=0


n = int(input())
board = [[0]*n for _ in range(n)]
check = [[0]*n for _ in range(n)]
min = 2147000000
max = -2147000000
sx = sy = ex = ey = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]<min:
            min = tmp[j]
            sx = i
            sy = j
        if tmp[j]>max:
            max = tmp[j]
            ex = i
            ey = j

        board[i][j]=tmp[j]


check[sx][sy]=1
cnt = 0

DFS(sx,sy)

print(cnt)