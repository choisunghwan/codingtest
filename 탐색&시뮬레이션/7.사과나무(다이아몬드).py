# 다이아몬드 모양안의 수 모두 더하기.
import sys
#sys.stdin=open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')

n = int(input()) # 자연수 n이 주어진다.

a = [list(map(int,input().split())) for _ in range(n)]

res = 0 # res를 합한 값을 담아두는 변수
s = e = n // 2 #s는 start , e는 end 

for i in range (n): # i는 행으로 0부터 시작해서 N번 반복
    for j in range(s, e+1): # j는 열로 s부터 e까지
        res += a[i][j] # 해당 행열 값을 
    if i < n//2: # 0 1 2 행 계산
        s-=1
        e+=1
    else: # 3 4 행 값 계산
        s+=1
        e-=1
print(res)
