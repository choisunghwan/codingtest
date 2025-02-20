# https://www.acmicpc.net/problem/7576

from collections import deque

#입력 받기
M,N = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]  # 위, 아래, 왼쪽, 오른쪽
dy = [0, 0, -1, 1]
 
print(tomato)

queue = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append((i,j))

while queue:
    x,y = queue.popleft() # 현재 위치 꺼내기

    for i in range(4): # 4방향 탐색
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 내에 있고, 안 익은 토마토(0)라면 익히기
        if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            queue.append((nx, ny))
    
#최소 날짜 계산
answer = 0 
for i in range(N):
    for j in range(M):
        if tomato[i][j] ==0: # 아직 안 익은 토마토가 있으면 -1 출력 후 종료
            print(-1)
            exit(0)
        answer = max(answer, tomato[i][j]) # 최대 날짜 찾기

print(answer -1) # 처음 시작 값이 1이므로 1빼줌줌


        