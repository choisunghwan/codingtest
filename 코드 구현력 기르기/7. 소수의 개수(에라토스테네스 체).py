import sys
# sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt') 

n = int(input()) # 자연수 n 입력
ch = [0] * (n+1) # 값이 0 인 리스트 만들기. 갯수는 n만큼.  <추가 설명: 인덱스 0부터 시작하기때문에 n+1로 해주어야 n개의 공간이 만들어진다.>
cnt = 0 #count = cnt  0으로 초기화

for i in range(2, n+1): # 2 부터 n 까지 i에 하나씩 넣으면서 반복. <추가 설명 : 1은 소수가 아니므로 2부터 시작한다.>
    if ch[i] == 0:
        cnt +=1
    for j in range(i, n+1, i): # start , end , step(1이면 1씩증가 2면 2씩증가)
        ch[j] = 1 # i 씩증가 했을때의 값에 1로 초기화 시켜준다.
print(cnt) #소수 개수 출력