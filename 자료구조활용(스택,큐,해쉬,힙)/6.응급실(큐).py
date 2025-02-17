import sys
from collections import deque
# 입력값: 5 2
#60 50 70 80 90
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')

n, m = map(int,input().split()) # 환자 수 n, 찾고 싶은 환자 위치 m
Q = deque(enumerate(map(int, input().split())))  # (환자 번호, 위험도) 저장
print(Q)
cnt = 0 # 몇 번째로 진료받는지 저장하는 변수

while True:
    cur = Q.popleft() # 가장 앞에 있는 환자 꺼냄

    # 중요도가 더 높은 환자가 있는지 확인
    # if any(cur[1] < x[1] for x in Q):
    if cur[1] < max(Q, key=lambda x: x[1])[1]:
        Q.append(cur)
    
    else:
        cnt +=1 # 진료받음
        if cur[0] == m: # 찾던 환자인 경우
            print(cnt)
            break


