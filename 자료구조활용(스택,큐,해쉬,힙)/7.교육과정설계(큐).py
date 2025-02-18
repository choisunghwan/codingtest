import sys
from collections import deque
# 입력 값
# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')

need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))
