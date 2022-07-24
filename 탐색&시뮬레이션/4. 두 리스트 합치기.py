import sys
#sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')

n = int(input()) # 리스트의 크기
a = list(map(int,input().split())) # 리스트 값 받음
m = int(input()) # 두번째 리스트 크기 받음
b = list(map(int,input().split())) # 리스트 값 받음

p1 = p2 = 0
c = []
while p1 < n and p2 < m : #p1, p2는 0으로 초기화 했던 값이므로 n과 m 리스트가 0이 아닌이상 반복문은 게속 돈다.
    if a[p1] <= b[p2]: 
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1

if p1 < n:
    c=c+a[p1:] #p1 부터 마지막 자료 까지
if p2 < m:
    c=c+b[p2:]

for x in c:
    print(x,end=' ')