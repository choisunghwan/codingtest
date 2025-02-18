import sys
from collections import deque
# 입력 값
# 5
# big
# good
# sky
# blue
# mouse
# sky
# good
# mouse
# big
sys.stdin=open("C:\\Users\\csh\\Documents\\코딩테스트\\자료구조활용(스택,큐,해쉬,힙)\\input.txt",'rt')

n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1

for i in range(n-1):
    word = input()
    p[word] = 0

for key,val in p.items():
    print(key,val)
    if val == 1:
        print(key)
        break