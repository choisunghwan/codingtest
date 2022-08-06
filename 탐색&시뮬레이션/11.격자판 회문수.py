import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')


board = [list(map(int,input().split())) for _ in range(7)]

cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]
        if tmp == tmp[::-1]: #회문 이라면
            cnt+=1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt+=1
print(cnt)