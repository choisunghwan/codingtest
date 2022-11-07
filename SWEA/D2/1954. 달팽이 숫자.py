import sys
sys.stdin = open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D2\\input.txt", 'rt')

T=int(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for test_case in range(1,T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    r, c=0, 0
    dist = 0

    for n in range(1, N*N+1):
        snail[r][c] = n 
        r += dr[dist]
        c += dc[dist]

        if r<0 or c<0 or r>=N or c>=N or snail[r][c]!=0:
            r-=dr[dist]
            c-=dc[dist]

            dist=(dist+1)%4

            r+= dr[dist]
            c+= dc[dist]
    print("#{}".format(test_case))
    for row in snail:
        print(*row)
    print()