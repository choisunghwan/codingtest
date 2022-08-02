import sys
sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')

n = int(input()) # 첫줄에 자연수 N이 주어진다.

a = [list(map(int,input().split())) for _ in range(n)] # 한줄을 읽어서 리스트화 시킴.거기에 for 문을 넣음으로써 n번 읽는다.


largest = -2147000000 # 가장 작은값으로 초기화 시킴.

# 행 열 합 구해서 최대합 추려내기
for i in range(n):
    sum1 = sum2 = 0 #sum1은 행의 합 , sum2는 열의합
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1 
    if sum2 > largest:
        largest = sum2

# 두 대각선 최대합 구하기  
sum1 = sum2 = 0
for i in range (n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1 
if sum2 > largest:
    largest = sum2

#최대합 출력
print(largest)