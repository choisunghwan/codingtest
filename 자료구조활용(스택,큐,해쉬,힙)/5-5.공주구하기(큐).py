import sys
from collections import deque
# 입력값: 8 3
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')
n, k = map(int,input().split())
print(n,k)

# 큐 초기화
dq= list(range(1,n+1))
dq = deque(dq)
print(dq)

# 요세푸스 순열 계산
while len(dq) > 1:
    for _ in range(k-1):
        cur = dq.popleft()  # 앞에서 빼서 뒤로 추가
        dq.append(cur)
    dq.popleft() # k번째 사람 제거

    
print(dq[0])