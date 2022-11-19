import sys
sys.stdin = open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D2\\input.txt", 'rt')

n = int(input()) # 1개의 정수가 주어진다.

for i in range(1, n+1): # 1~100
    i = str(i)
    clap = i.count('3') + i.count('6') + i.count('9')

    if clap == 0:
        print(i , end=" ")
    else:
        print("-" * clap, end=" ")


# 다른 풀이법


# num = int(input()) # 정수 입력 값을 num 변수에 담아둠.
# ans = '' # 문자열 변수 (출력 값을 담을 변수)
# condition = ['3','6','9'] # 문자열 3, 6, 9 를 condition 이라는 리스트 변수에 담아둠

# for n in range(1, num+1): # 1부터 num(입력받은 수) 까지  하나씩 반복
#     cnt = 0 # 정수형 변수
#     digit = str(n) # 1~num 까지의 수를 하나씩 뽑아서 n이라는 변수에 담는데, 변수 n을 문자로 바꾸어서 digit 라는 변수에 저장.
#     for d in digit: # digit 변수에서 하나씩 뽑아 d에 넣고
#         if d in condition: # 만약 변수 d 가 condition 이라는 리스트 변수에 있는 값과 동일한 값이 있다면
#             cnt += 1 # cnt변수 에 1을 더해줌.
#     if cnt == 0: # 만약 cnt 변수 값이 0이라면
#         ans += digit # 문자열 변수 ans 에 digit 를 추가해서 저장함.
#     else: # 만약 cnt 변수 값이 0이 아니라면
#         for _ in range(0, cnt): # 0~ cnt-1 까지 반복
#             ans += '-' # - 문자 추가하기
#     ans += ' ' # 띄어 쓰기

# print(ans) # 출력