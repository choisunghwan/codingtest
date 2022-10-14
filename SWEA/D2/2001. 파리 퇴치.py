import sys
sys.stdin=open("C:\\Users\\csh\\Documents\\pycharmCodingTest\\input.txt",'rt')

# 테스트케이스의 개수 입력받기
t = int(input())

# 1부터 입력받은 테스트 케이스의 개수 만큼 반복하기.
for test_case in range(1, t+1):
    n, m = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for si in range(n-m+1):
        for sj in range(n-m+1):
            cnt = 0
            for i in range(si, si + m):
                for j in range(sj, sj + m):
                    cnt += data[i][j]
            if cnt > answer:
                answer = cnt
    print(f'#{test_case} {answer}')
