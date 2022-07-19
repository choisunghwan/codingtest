import sys
# sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt')

n = int(input()) # 문제의 개수
a = list(map(int, input().split())) # 0 1 입력

sum = 0
cnt = 0

for x in a: # 리스트 a에서 하나씩 x 에 입력
    if x == 1: # x 가 1이라면
        cnt += 1 #가중치 1을 더하고
        sum +=cnt # sum에 cnt 값을 더해줌
    else:
        cnt = 0 # x가 1 이 아니라면 가중치 0으로 
print(sum) # sum(점수) 출력



