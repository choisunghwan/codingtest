import sys
#sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\코드 구현력 기르기\\input.txt",'rt') 

n, m = map(int, input().split()) # 자연수 n 과 m 이 입력받음

cnt = [0] * (n + m + 3) #n+m 크기만큼의 리스트가 만들어지고 안의 값은 0으로 초기화
max = -2147000000

#카운터
for i in range(1, n+1): # 1부터 n 까지 반복
    for j in range(1, m+1): # 1부터 m까지 반복
        cnt[i+j] += 1

#최댓값 찾기
for i in range(n + m + 1): # 0부터 n+m번 반복
    if cnt[i] > max: # 카운트 횟수가 0부터 비교하면서 가장 큰 값을 찾아냄.
        max = cnt[i]

#최댓값과 동일한 값 모두 출력
for i in range(n + m + 1): # 0부터 n+m번 반복
    if cnt[i] == max: # 최댓값과 동일하다면
        print(i , end=' ') # 출력해준다.