import sys
from collections import deque
# 입력값: 8 3
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')
n, k = map(int,input().split())
print(n,k)

dq= list(range(1,n+1))
dq = deque(dq)
print(dq)

while dq:
    for _ in range(k-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        dq.popleft()