import sys
sys.stdin = open("C:\\Users\\csh\\Desktop\\코딩테스트\\SWEA\\D2\\input.txt", 'rt')

# 테스트케이스의 개수 입력받기
T = int(input())

# 1부터 입력받은 테스트 케이스의 개수 만큼 반복하기. 
for test_case in range(1, T+1):
    # 주어지는 문자열 N의 개수 입력받기 
    n = int(input())
    # 주어진 문자열을 리스트에 담아서 변수 data에 할당하기.
    data = list(map(int, input().split()))
    # 오름차순(기본)정렬시키기
    data.sort()
    
    # 테스트 케이스 줄바꿈없이 출력
    print("#%d" %test_case, end=' ')
    # 정렬된 문자열을 문자열개수(n)만큼 하나씩 j에 담아서 줄바꿈없이 출력
    for j in range(n):
        print(data[j],end=' ')
    #줄바꿈
    print()



