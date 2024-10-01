from collections import deque

def solution(maps):
    # 상, 하, 좌, 우로 이동할 좌표 변화값
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 맵의 크기
    n = len(maps)
    m = len(maps[0])

    # BFS를 위한 큐 초기화 (시작점 (0, 0))
    queue = deque([(0, 0)])

    # BFS 시작
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 상, 하, 좌, 우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵을 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽(0)인 경우 무시
            if maps[nx][ny] == 0:
                continue

            # 처음 방문하는 노드인 경우에만 최단 거리를 기록
            if maps[nx][ny] == 1:
                # 현재 노드까지의 거리 + 1
                maps[nx][ny] = maps[x][y] + 1

                # 큐에 넣어 다음에 방문할 노드로 설정
                queue.append((nx, ny))

                # 목적지에 도달한 경우, 즉시 반환
                if nx == n-1 and ny == m-1:
                    return maps[nx][ny]

    # 목적지에 도달할 수 없는 경우
    return -1

# 입력 데이터
maps = [[1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]]

# 결과 출력
result = solution(maps)
print(result)  # 출력: 11
