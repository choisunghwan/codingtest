import sys
from collections import deque


# 7
# 1 0 1 0 0 1 1
# 1 0 0 0 1 1 1
# 0 0 1 1 1 1 1
# 0 1 0 0 0 1 1
# 0 0 1 0 1 1 0
# 1 1 0 0 0 0 0
# 1 0 1 1 1 0 0
sys.stdin = open("C:/Users/csh/Documents/코딩테스트/BFS/input.txt", "r")

# 방향 벡터 (상,하,좌,우,대각선)
dx = [-1,-1,0,0,-1,-1,1,1]
dy = [0, 0,-1,1,-1,1,-1,1]


# BFS 함수 정의
def bfs(x, y, n, grid, visited):
    queue = deque([(x, y)])
    visited[x][y] = True  # 방문 처리

    while queue:
            cx, cy = queue.popleft()  # 큐에서 하나 꺼내기

            # 8방향 탐색 (상, 하, 좌, 우, 대각선)
            for i in range(8):
                nx = cx + dx[i]
                ny = cy + dy[i]

                # 범위 안에 있고, 방문처리 안 했으면, 섬(1)인 경우
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


# 1. 입력 받기
n = int(input())  # 지도 크기
grid = [list(map(int, input().split())) for _ in range(n)]  # 지도 데이터
visited = [[False] * n for _ in range(n)]  # 방문 여부

island_count = 0  # 섬 개수

# 2. 반복문을 돌면서 섬을 찾는다. (BFS 함수 호출)
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:  # 새로운 섬 발견
            bfs(i, j, n, grid, visited)
            island_count += 1

print(island_count)
