import sys
from collections import deque
sys.stdin = open("C:/Users/csh/Documents/코딩테스트/BFS/input.txt", "r")
# 미로의 최단거리 통로 (BFS)
# 입력예제
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 0
# 출력예제
# 12

dx = [-1,0,1,0] # 방향 탐색
dy = [0,1,0,-1] # 방향 탐색

board = [list(map(int,input().split())) for _ in range(7)] # 미로 입력받기
dis = [[0]*7 for _ in range(7)] # 거리계산 리스트

q = deque() # deque 생성
q.append((0,0)) # 시작점 deque에 넣기
board[0][0] = 1 # 시작점 방문처리

while q: # deque가 빌때까지 반복
    tmp = q.popleft() # deque에서 좌표 꺼내기
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            q.append((x,y))

if dis[6][6] == 0: # 도착점에 도달하지 못했다면
    print(-1) # -1 출력
else:
    print(dis[6][6]) # 도착점까지의 거리 출력
