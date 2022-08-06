import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

a.insert(0,[0]*n) # 0번 행에다가 0으로 초기화된 값을 n개 삽입한다.
a.append([0]*n) #0번으로 초기화된 값을 n개 를 마지막행에 넣어줌

for x in a:
    x.insert(0, 0) 
    x.append(0)

cnt = 0
for i in range (1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)): # all() 함수는 ()안에 조건이 모두 참일경우 참이 된다.
            cnt+=1
print(cnt)