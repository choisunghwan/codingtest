import sys
#sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\탐색&시뮬레이션\\input.txt",'rt')

s = input() # 문자와 숫자가 섞인 문자열
res = 0
for x in s:
    if x.isdecimal(): # x 가 0-9까지의 수가 맞다면 <- 조건
        res = res*10+int(x) #1. res 는 0 이므로 처음에 int(X) 값만 res에 저장 2. int(X)값에 10을 곱한후 다음 int(X)를 더한다

print(res) 

cnt = 0 #개수

for i in range(1, res+1): # 1에서 res(자기자신) 까지
    if res % i == 0: #res를 i로 나누었을때 나누어 떨어지면 약수이므로
        cnt += 1
print(cnt)
