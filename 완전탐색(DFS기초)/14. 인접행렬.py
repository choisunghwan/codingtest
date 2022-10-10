import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\pycharmCodingTest\\input.txt",'rt')

n,m = map(int, input().split()) # 입력 n,m
g=[[0]*(n+1) for _ in range(n+1)] # g
for i in range(m):
    a, b, c = map(int,input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()