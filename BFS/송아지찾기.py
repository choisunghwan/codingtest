import sys
from collections import deque
sys.stdin = open("C:/Users/csh/Documents/코딩테스트/BFS/input.txt", "r")
# 5 14 
# 송아지 찾기 (BFS)

MAX = 10000
ch = [0] * (MAX + 1) # 방문여부 확인
dis = [0] * (MAX + 1) # 송아지까지의 거리

n,m = map(int,input().split()) #   n: 현수의 위치, m: 송아지의 위치

ch[n] = 1 # 현수의 위치 방문처리
dis[n] = 0 # 현수의 위치까지의 거리는 0

dq = deque() # deque 생성
dq.append(n) # 현수의 위치를 deque에 넣기

while dq: # deque가 빌때까지 반복

    now = dq.popleft() # 현수의 위치를 deque에서 꺼내기

    if now == m: # 송아지의 위치에 도착하면 종료
        break # 송아지의 위치에 도착하면 종료

    for next in (now -1, now +1 , now +5): # 세가지 경우의 수
        if 0 < next <= MAX: # 범위안에 있을때
            if ch[next] == 0: # 방문하지 않았다면
                dq.append(next) # deque에 넣기
                ch[next] = 1 # 방문처리
                dis[next] = dis[now] + 1 # 거리계산

print(dis[m]) # 송아지까지의 거리 출력
