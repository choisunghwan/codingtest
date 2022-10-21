import sys
sys.stdin = open("C:\\Users\\csh\\Documents\\코딩테스트\\SWEA\\D3\\input.txt", 'rt')
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
# ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    h = list(map(int,input().split()))
    result = 0

    for i in range(2, n-2):
        around = max([h[i-2],h[i-1],h[i-1],h[i+1],h[i+2]])
        if(h[i] > around):
            result += h[i]-around
    print(f"#{test_case} {result}")