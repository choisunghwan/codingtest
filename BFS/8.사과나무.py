import sys
from collections import deque

#입력예제
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

#출력예제
# 379

sys.stdin = open("C:/Users/csh/Documents/코딩테스트/BFS/input.txt", "r")    

# 방향 탐색
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 1. 입력받기
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
#방문유무 체크리스트
visited = [[False] * n for _ in range(n)] # 방문 여부 확인 리스트

sum = 0 # 수확된 사과의 총 개수

Q = deque() # BFS에 사용할 큐

visited[n//2][n//2] = True # 중앙은 방문처리
sum += grid[n//2][n//2] # 중앙 사과는 이미 수확 
Q.append((n//2, n//2)) # 큐에 중앙 위치 넣기

L = 0  # BFS 레벨, 다이아몬드의 넓이를 확장하는 변수

while True:
    if L == n // 2: # 다이아몬드 모양을 다 탐색했다면 종료
        break
    for _ in range(len(Q)): # 큐 크기만큼 반복
        tmp = Q.popleft() # 큐에서 하나의 좌표 꺼내기
        for d in range(4): # 네방향 탐색
            nextX = tmp[0] + dx[d]
            nextY = tmp[1] + dy[d]
            if not visited[nextX][nextY]: # 아직 방문하지 않았다면
                sum += grid[nextX][nextY] # 사과 수확
                visited[nextX][nextY] = True # 방문처리
                Q.append((nextX, nextY)) # 큐에 넣기
    L += 1 # 탐색 범위 확장
print(sum) # 결과 출력