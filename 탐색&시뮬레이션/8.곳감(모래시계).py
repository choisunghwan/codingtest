import sys
#sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')

n = int(input()) # N*N 격자판에서 N 값 입력
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())

for i in range (m):
    # h: 행번호 , t: 방향 k: 회전명령 
    h,t,k  = map(int,input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) # a[h-1]행에 마지막 값을 pop 해서 0번자리에 insert 한다.

res = 0
s = 0
e = n-1

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
        
